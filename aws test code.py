import boto3
import requests
from flask import Flask, request, jsonify
import subprocess
import tempfile
from flask_cors import CORS
import uuid
import sys
import os

app = Flask(__name__)
CORS(app)


class VideoProcessingService:
    def __init__(self):
        pass
        # self.ml_client = MachineLearningApiClient()

    def process_video(self, video_data):
        emotion_tags = self.ml_client.predict_emotion(video_data)
        return emotion_tags
    

# service to upload video to S3 and other data to DynamoDB
class VideoStoringService:
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
    
    # def store_video(self, video_data, tags, patient_name, therapist_name):
    def store_video(self, video_data, patient_name, therapist_name):
        
        key = patient_name+'-'+str(uuid.uuid4())
        
        
        # put video and thumbnail in AWS S3 database
        bucket = boto3.resource('s3').Bucket('mcs21fyp')
        bucket.put_object(Key=key, Body=video_data)
        video_data.seek(0)  # Reset the file pointer to the beginning after reading

        thumbnail = self.extract_thumbnail(video_data)
        bucket.put_object(Key=key+'_thumbnail', Body=thumbnail)
        
        # put metadata in AWS dynamoDB database
        table = boto3.resource('dynamodb').Table('mcs21fyp')
        input = {
            'key': key,
            # 'tags': tags,
            'patientName': patient_name,
            'therapistName': therapist_name,
        }
        table.put_item(Item=input)
        return None


video_processing_service = VideoProcessingService()
video_storing_service = VideoStoringService()


# def use_model(video):
#     # preprocessing + call model here
#     return emotion_tags


# controller for feeding video to model and uploading to database
@app.route('/upload_video', methods=['POST'])
def process_video():
    try:
        video_data = request.files['video']
        patient_name = request.form.get('patient_name')
        therapist_name = request.form.get('therapist_name')
        
        # emotion_tags = use_model(video_data)

        video_storing_service.store_video(video_data, patient_name, therapist_name)
        return jsonify({'message': 'Video uploaded successfully'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

    # return jsonify({"emotion_tags": emotion_tags})


# import requests

# class MachineLearningApiClient:
#     def __init__(self):
#         self.ml_api_endpoint = # "http://your_ml_server/predict";

#     def predict_emotion(self, video_data):
#         response = requests.post(self.ml_api_endpoint, json={"video_data": video_data})
        
#         if response.status_code == 200:
#             prediction_result = response.json()
#             emotion_tags = prediction_result.get("emotion_tags", "Emotion tags not available")
#             return emotion_tags
#         else:
#             return "Error processing video"
        

# service that returns the video that the user clicks on
class GetVideoService:  
    def get_video(self, video_key):
        # get video from AWS S3 bucket
        bucket = boto3.resource('s3').Bucket('mcs21fyp')
        video = bucket.get_object(Key=video_key).body

        # get metadata from AWS dynamoDB database
        table = boto3.resource('dynamodb').Table('mcs21fyp')
        response = table.get_item(Key={'key': {'S': video_key}})

        metadata = {
            'tags': response.tags,
            'patientName': response.patient_name,
            'therapistName': response.therapist_name,
        }

        return video, metadata


get_video_service = GetVideoService()

# controller for retrieving video based on key provided
@app.route('/display_video', methods=['POST'])
def get_video():
    video_key = request.form.get('video_key')

    video, metadata = get_video_service.get_video(video_key)

    response_data = {
        'video': video,
        'tags': metadata.tags,
        'patientName': metadata.patient_name,
        'therapistName': metadata.therapist_name,    
    }

    return jsonify(response_data)


# service that gets a list of all thumbnails with their corresponding video's metadata
class GetAllVideosService:
    def get_all_videos(self):
        bucket = boto3.resource('s3').Bucket('mcs21fyp')
        table = boto3.resource('dynamodb').Table('mcs21fyp')
        data = []

        for obj in bucket.objects.all():
            if obj.key.endswith("_thumbnail"):
                key = obj.key
                thumbnail = bucket.get_object(Key=key).body
                video_key = key.replace("_thumbnail", '')  # remove "thumbnail" from end of key so that it becomes corresponding video's key
                response = table.get_item(Key={'key': {'S': video_key}})
                metadata = {
                    # 'tags': response.tags,
                    'patientName': response.patient_name,
                    'therapistName': response.therapist_name,
                }
                data.append({
                    video_key: video_key,
                    thumbnail: thumbnail,
                    metadata: metadata,
                    })

        return data


get_all_videos_service = GetAllVideosService()


# controller for retrieving all videos
@app.route('/all_videos', methods=['GET'])
def get_all_videos():
    all_videos = get_all_videos_service.get_all_videos()

    return jsonify(all_videos)


if __name__ == '__main__':
    app.run()