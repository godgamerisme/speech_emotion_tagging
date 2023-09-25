import boto3
from flask import Flask, request, jsonify
import subprocess
import tempfile


class VideoProcessingService:
    def __init__(self):
        pass
        # self.ml_client = MachineLearningApiClient()

    def process_video(self, video_data):
        emotion_tags = self.ml_client.predict_emotion(video_data)
        return emotion_tags
    

# service to upload video to S3 and other data to DynamoDB
class VideoStoringService:
    def store_video(self, video_data, tags, patient_name, therapist_name):
        key = 1  # incremental counter
        thumbnail = self.extract_thumbnail(video_data)

        # put video and thumbnail in AWS S3 database
        bucket = boto3.resource('s3').Bucket('mcs21fyp')
        bucket.put_object(Key=key, Body=video_data)
        bucket.put_object(Key=key+'_thumbnail', Body=thumbnail)

        # put metadata in AWS dynamoDB database
        table = boto3.resource('dynamodb').Table('mcs21fyp')
        input = {
            'key': key,
            'video': video_data,
            'tags': tags,
            'patientName': patient_name,
            'therapistName': therapist_name,
        }
        table.put_item(Item=input)


    def extract_thumbnail(self, video):
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{video['format']}", mode="wb") as temp_video:
            temp_video.write(video["data"].decode("base64"))

        # Run FFmpeg to extract the thumbnail from the temporary video file
        ffmpeg_cmd = [
            'ffmpeg',
            '-i', temp_video.name,  # Input video file
            '-ss', str(10),  # Seek to the specified time
            '-vframes', '1',  # Extract only 1 frame (the thumbnail)
            '-f', 'image2pipe',  # Output format
            '-'  # Send the output to stdout
        ]

        try:
            thumbnail_data = subprocess.check_output(ffmpeg_cmd)
            # print('Thumbnail extracted successfully.')
        
            # Now, 'thumbnail_data' contains the thumbnail image data as bytes.
            # You can store it in a variable or a database.

        except subprocess.CalledProcessError as e:
            print(f'Error: {e}')
        finally:
            # Clean up the temporary video file
            temp_video.close()
            temp_video.unlink()

        return thumbnail_data



app = Flask(__name__)
video_processing_service = VideoProcessingService()
video_storing_service = VideoStoringService()


# controller for feeding video to model and uploading to database
@app.route('/process_video', methods=['POST'])
def process_video():
    data = request.json
    video_data = data.get('video_data')
    patient_name = data.get('patient_name')
    therapist_name = data.get('therapist_name')

    emotion_tags = video_processing_service.process_video(video_data)
    video_storing_service.store_video(video_data, emotion_tags, patient_name, therapist_name)

    # return jsonify({"emotion_tags": emotion_tags})


import requests

class MachineLearningApiClient:
    def __init__(self):
        self.ml_api_endpoint = # "http://your_ml_server/predict";

    def predict_emotion(self, video_data):
        response = requests.post(self.ml_api_endpoint, json={"video_data": video_data})
        
        if response.status_code == 200:
            prediction_result = response.json()
            emotion_tags = prediction_result.get("emotion_tags", "Emotion tags not available")
            return emotion_tags
        else:
            return "Error processing video"
        

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
    data = request.json
    video_key = data.get('video_key')

    video, metadata = get_video_service.get_video(video_key)

    response_data = {
        'video': video,
        'tags': metadata.tags,
        'patientName': metadata.patient_name,
        'therapistName': metadata.therapist_name,    
    }

    return jsonify(response_data)


# service that gets all videos
class GetAllVideosService:
    def get_all_videos(self):
        bucket = boto3.resource('s3').Bucket('mcs21fyp')
        table = boto3.resource('dynamodb').Table('mcs21fyp')
        data = []

        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            data.extend(response['Items'])

        # get video from AWS S3 bucket
        for video in data:
            video_data = bucket.get_object(Key=video.key).body
            video[video_data] = video_data

        return data


get_all_videos_service = GetAllVideosService()


# controller for retrieving all videos
@app.route('/all_videos', methods=['GET'])
def get_all_videos():
    data = request.json

    videos = get_all_videos_service.get_all_videos()

    response_data = {
        "videos": videos,
    }

    return jsonify(response_data)


if __name__ == '__main__':
    app.run()