import boto3
import requests
from flask import Flask, request, jsonify
import subprocess
import tempfile
from flask_cors import CORS
import uuid
import sys
import os
from run_model import EmotionPredictor
from preprocessing import PreprocessVideo
import datetime
from werkzeug.datastructures import FileStorage

app = Flask(__name__)
CORS(app)
    

# service to upload video and thumbnail to S3 and other data to DynamoDB
class StoreVideoService:
    def extract_thumbnail(self, video):
        video_format = video.filename.rsplit('.', 1)[1].lower()

        try:
            # Create a temporary directory for the video file
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_video_path = os.path.join(temp_dir, f"temp_video.{video_format}")

                # Write the file data to the temporary video file
                with open(temp_video_path, "wb") as temp_video:
                    file_data = video.read()
                    temp_video.write(file_data)

                # Run FFmpeg to extract the thumbnail from the temporary video file
                ffmpeg_cmd = [
                    'ffmpeg',
                    '-i', temp_video_path,  # Input video file
                    '-ss', str(10),  # Seek to the specified time
                    '-vframes', '1',  # Extract only 1 frame (the thumbnail)
                    '-f', 'image2pipe',  # Output format
                    '-'
                ]

                thumbnail_data = subprocess.check_output(ffmpeg_cmd)
                print('Thumbnail extracted successfully.', file=sys.stderr)

                return thumbnail_data

        except Exception as e:
            print(f'Error: {e}', file=sys.stderr)
            return None
    

    def store_video(self, video_data, patient_name, therapist_name, emotion_tags, age, gender):
        test_date='12/12/2023'
        key = patient_name+'-'+str(uuid.uuid4())
        
        # put video and thumbnail in AWS S3 database
        bucket = boto3.resource('s3').Bucket('mcs21fyp')
        bucket.put_object(Key=key, Body=video_data)
        video_data.seek(0)  # Reset the file pointer to the beginning after reading

        thumbnail = self.extract_thumbnail(video_data)
        bucket.put_object(Key=key+'_thumbnail', Body=thumbnail)
        
        # put metadata in AWS dynamoDB database
        table = boto3.resource('dynamodb').Table('mcs21fyp')
        today_date = datetime.date.today().strftime("%m/%d/%Y")
        input = {
            'key': key,
            'patientName': patient_name,
            'therapistName': therapist_name,
            'emotionTags': emotion_tags,
            'age': age,
            'gender': gender,
            'date': today_date,
            # 'date': test_date,
        }
        table.put_item(Item=input)
        return None


store_video_service = StoreVideoService()


# controller for feeding video to model and uploading data to S3 and DynamoDB
@app.route('/upload_video', methods=['POST'])
def process_video():
    """
     This API endpoint takes in a video file and process the video to predict the emotion tags and upload the video to S3 and the metadata to DynamoDB
    """
    try:
        video_file  = request.files['video']
        patient_name = request.form.get('patient_name')
        therapist_name = request.form.get('therapist_name')
        age = request.form.get('age')
        gender = request.form.get('gender')

        # emotion_tags = use_model(videodata)
        clear_directory("./backend/video")

        filename = video_file.filename
        destination_path = './backend/video/' + filename
        video_file.save(destination_path)
        
        video_preprocessor = PreprocessVideo(video_path=destination_path)
        preprocessed_audio_array,corrupted_audio_index = video_preprocessor.get_preprocessed_audio_array()
        audio_duration = video_preprocessor.get_duration()
        emotion_predictor = EmotionPredictor()
        emotion_tags = emotion_predictor.predict_emotions(preprocessed_audio_array,audio_duration,corrupted_audio_index)
        
        # check if its an avi file
        if is_avi_file(filename):
            # use ffmpeg to convert to mp4
            print("converting to mp4")
            try:
                subprocess.run(['ffmpeg', '-i', destination_path, destination_path.replace(".avi", ".mp4")],check=True)
                destination_path = destination_path.replace(".avi", ".mp4")
                video_file = FileStorage(stream=open(destination_path, "rb"),filename=filename.replace(".avi", ".mp4"))
            except Exception as e:
                print("error converting to mp4")
                return jsonify({'error': str(e)}), 500
        video_file.seek(0)
        store_video_service.store_video(video_file, patient_name, therapist_name, emotion_tags, age, gender)
        video_file.close()
        print("store success")
        video_preprocessor.clear_all_directories()

        response = {'message': 'Video uploaded successfully'}
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

def is_avi_file(filename):
    # Check the file extension
    _, file_extension = os.path.splitext(filename)
    return file_extension.lower() == '.avi'
    


# service that returns the data corresponding to video key passed to it
class GetVideoService:  
    def get_video(self, video_key):
        # get video from AWS S3 bucket
        s3 = boto3.client('s3')
        
        # get metadata from AWS dynamoDB database
        table = boto3.resource('dynamodb').Table('mcs21fyp')
        response = table.get_item(Key={'key': video_key})

        url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': 'mcs21fyp', 'Key': video_key},
        ExpiresIn=99999  # URL will expire in 99999 seconds
        )

        metadata = {
            'url': url,
            'patientName': response['Item']['patientName'],
            'age': response['Item']['age'],
            'therapistName': response['Item']['therapistName'],
            'gender': response['Item']['gender'],  
            'date': response['Item']['date'],
            'emotionTags': response['Item']['emotionTags'],            
        }
        return metadata


get_video_service = GetVideoService()

# controller for retrieving video based on key provided
@app.route('/get_video', methods=['POST'])
def get_video():
    video_key = request.form.get('video_key')

    metadata = get_video_service.get_video(video_key)

    return jsonify(metadata)


# service that gets a list of all thumbnails with their corresponding video's metadata
class GetAllVideosService:
    def get_all_videos(self):
        s3 = boto3.client('s3')  # Create an S3 client

        # List objects in the bucket and filter for thumbnails
        thumbnails = [obj for obj in s3.list_objects(Bucket='mcs21fyp')['Contents'] if obj['Key'].endswith("_thumbnail")]

        table = boto3.resource('dynamodb').Table('mcs21fyp')
        data = []

        for thumbnail in thumbnails:
            key = thumbnail['Key']
            video_key = key.replace("_thumbnail", '')  # remove "thumbnail" from end of key so that it becomes corresponding video's key
            response = table.get_item(Key={'key': video_key})
            item = response.get('Item')  # Get the DynamoDB item from the response
            if item:
                metadata = {
                    'patientName': item.get('patientName'),
                    'therapistName': item.get('therapistName'),
                    'date': item.get('date'),
                    'age': item.get('age'),
                }
                data.append({
                    'video_key': video_key,
                    'thumbnail_key': key,
                    'metadata': metadata,
                })

        return data


get_all_videos_service = GetAllVideosService()


# controller for retrieving all videos
@app.route('/all_videos', methods=['GET'])
def get_all_videos():
    all_videos = get_all_videos_service.get_all_videos()

    return jsonify(all_videos)


def clear_directory(directory_path):
        # Ensure the path exists
        if not os.path.exists(directory_path):
            print(f"The directory '{directory_path}' does not exist.")
            return

        # List all files in the directory
        file_list = os.listdir(directory_path)

        # Remove each file
        for file_name in file_list:
            file_path = os.path.join(directory_path, file_name)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    # If you also want to remove subdirectories and their contents, uncomment the line below
                    # shutil.rmtree(file_path)
                    pass
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

        print(f"All files in '{directory_path}' have been deleted.")


if __name__ == '__main__':
    app.run()