from preprocessing import PreprocessVideo
from keras.models import model_from_json
import pandas as pd
import datetime
import os

class EmotionPredictor:
    def __init__(self):
        self.model = self.load_model()

    def load_model(self):
        #check if model exist
        if not os.path.exists('./backend/model/Audio_2DCNN_4L_R2.json'):
            print("Model does not exist")
            return
        model_file = open('./backend/model/Audio_2DCNN_4L_R2.json', 'r')
        model_json = model_file.read()
        model_file.close()
        model = model_from_json(model_json)
        model.load_weights('./backend/model/Audio_2DCNN_4L_R2.h5')
        return model
    
    def predict_emotions(self,preprocessed_audio_array,audio_duration,corrupted_audio_index=None):
        """
         This function takes in the preprocessed audio array and uses the model to predict the emotion tags 
          and returns the emotion tags in timeframe HH:MM:SS format
        """
        # Replace this with your actual emotion prediction logic
        emotion_tags = self.model.predict(preprocessed_audio_array,batch_size=16,verbose=1)
        emotion_tags = emotion_tags.argmax(axis=1)
        label_mapping_df = pd.read_csv('./backend/model/label_mapping.csv')
        label_mapping_dict = dict(zip(label_mapping_df['EncodedLabel'], label_mapping_df['OriginalLabel']))
        emotion_tags = [label_mapping_dict[x] for x in emotion_tags]
        emotion_tags = [emotion.split('_')[1] for emotion in emotion_tags ]

        if corrupted_audio_index:
            # replace emotion tags of corrupted audio with 'No Emotion'
            for index in corrupted_audio_index:
                emotion_tags[index] = 'No Emotion' 

        ret_emotions = []
        frame_duration = 3
        start_time = 0
        end_time = 0
        for i in range(len(emotion_tags)):
            #starttime is in seconds
            start_time = i*frame_duration
            #convert starttime to 00.00 format
            str_start_time = str(datetime.timedelta(seconds=start_time)).split('.')[0]
            
            #if its the last one, endtime is the remaining duration of audio
            if i == len(emotion_tags)-1:
                print("audio duration",audio_duration)
                end_time = audio_duration
            else:
                end_time = start_time + frame_duration
            #convert endtime to 00.00 format
            str_end_time = str(datetime.timedelta(seconds=end_time)).split('.')[0]

            #check if str_start_time is equals to the end time of the last element in ret_emotions
            #check the current emotion tag is the same as the emotion tags in the last element in ret_emotions
            #if yes, add the current end time - start time to the last element in ret_emotions 
            if len(ret_emotions) > 0 and ret_emotions[-1]['end_time'] == str_start_time and ret_emotions[-1]['emotion'] == emotion_tags[i]:
                #get the end time of the last element in ret_emotions
                last_end_time = ret_emotions[-1]['end_time']
                #convert last_end_time to seconds
                last_end_time = datetime.datetime.strptime(last_end_time, '%H:%M:%S')
                last_end_time = last_end_time.hour*3600 + last_end_time.minute*60 + last_end_time.second
                #add the current end time - start time to last_end_time
                last_end_time += (end_time - start_time)
                #convert last_end_time to 00.00 format
                last_end_time = str(datetime.timedelta(seconds=last_end_time)).split('.')[0]
                #update the end time of the last element in ret_emotions
                ret_emotions[-1]['end_time'] = last_end_time
            else:
                ret_emotions.append({
                    'begin_time': str_start_time, 
                    'end_time':  str_end_time,
                    'emotion': emotion_tags[i]
                })  
        return ret_emotions

if __name__ == "__main__":
    # Audio input path
    video_path = "./backend/video/Ses01F_impro01.avi"
    video_preprocessor = PreprocessVideo(video_path=video_path)
    preprocessed_audio_array,corrupted_audio_index = video_preprocessor.get_preprocessed_audio_array()
    audio_duration = video_preprocessor.get_duration()
    emotion_predictor = EmotionPredictor()
    emotion_tags = emotion_predictor.predict_emotions(preprocessed_audio_array,audio_duration,corrupted_audio_index)
    #print array of emotion tags
    for emotion_tag in emotion_tags:
        print(emotion_tag)

    