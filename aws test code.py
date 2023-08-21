import boto3
from flask import Flask, request, jsonify

# TODO - client, service, controller for all videos page (request for thumbnails, filtering, etc)
# TODO - client, service, controller for video page (display video)

class VideoProcessingService:
    def __init__(self):
        pass
        # self.ml_client = MachineLearningApiClient()

    def process_video(self, video_data):
        emotion_tags = self.ml_client.predict_emotion(video_data)
        return emotion_tags
    

class VideoStoringService:
    def store_video(self, video_data, tags, patient_name, therapist_name):
        key = 1  # incremental counter

        # put video in AWS S3 database
        s3 = boto3.resource('s3')
        s3.Bucket('mcs21fyp').put_object(Key=key, Body=video_data)

        # put metadata in AWS dynamoDB database
        dynamoDB = boto3.resource('dynamodb')
        table = dynamoDB.Table('mcs21fyp')
        input = {
            'Key': key,
            'Video': video_data,
            'Tags': tags,
            'PatientName': patient_name,
            'TherapistName': therapist_name,
        }
        table.put_item(Item=input)


app = Flask(__name__)
video_processing_service = VideoProcessingService()
video_storing_service = VideoStoringService()

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
        self.ml_api_endpoint = # "http://your_ml_server/predict"

    def predict_emotion(self, video_data):
        response = requests.post(self.ml_api_endpoint, json={"video_data": video_data})
        
        if response.status_code == 200:
            prediction_result = response.json()
            emotion_tags = prediction_result.get("emotion_tags", "Emotion tags not available")
            return emotion_tags
        else:
            return "Error processing video"
        

if __name__ == '__main__':
    app.run()