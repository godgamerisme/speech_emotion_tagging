from preprocessing import PreprocessVideo
from keras.models import model_from_json
import pandas as pd
import datetime

class EmotionPredictor:
    def __init__(self):
        # Load your emotion prediction model here (replace this with your actual loading logic)
        self.model = self.load_model()

    def load_model(self):
        model_file = open('./model/Audio_2DCNN_4L_R2.json', 'r')
        model_json = model_file.read()
        model_file.close()
        model = model_from_json(model_json)
        model.load_weights('./model/Audio_2DCNN_4L_R2.h5')
        return model
    
    def predict_emotions(self,preprocessed_audio_array,audio_duration,corrupted_audio_index=None):
        # Replace this with your actual emotion prediction logic
        emotion_tags = self.model.predict(preprocessed_audio_array,batch_size=16,verbose=1)
        emotion_tags = emotion_tags.argmax(axis=1)
        label_mapping_df = pd.read_csv('./model/label_mapping.csv')
        label_mapping_dict = dict(zip(label_mapping_df['EncodedLabel'], label_mapping_df['OriginalLabel']))
        emotion_tags = [label_mapping_dict[x] for x in emotion_tags]
        if corrupted_audio_index:
            # replace emotion tags of corrupted audio with 'No Emotion'
            for index in corrupted_audio_index:
                emotion_tags[index] = 'No Emotion' 

        ret_emotions = []
        frame_duration = 3
        for i in range(len(emotion_tags)):
            #if its the last one, endtime is the remaining duration of audio
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
            ret_emotions.append({
                'begin_time': str_start_time, 
                'end_time':  str_end_time,
                'emotion': emotion_tags[i]
            })  
        return ret_emotions

if __name__ == "__main__":
    # Audio input path
    video_path = "./video/Ses01F_impro01.avi"
    video_preprocessor = PreprocessVideo(video_path=video_path)
    preprocessed_audio_array,corrupted_audio_index = video_preprocessor.get_preprocessed_audio_array()
    audio_duration = video_preprocessor.get_duration()
    emotion_predictor = EmotionPredictor()
    emotion_tags = emotion_predictor.predict_emotions(preprocessed_audio_array,audio_duration,corrupted_audio_index)
    #print array of emotion tags
    for emotion_tag in emotion_tags:
        print(emotion_tag)

    