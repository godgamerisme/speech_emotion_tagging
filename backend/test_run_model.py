import unittest
from unittest.mock import patch, mock_open
import pandas as pd
from preprocessing import PreprocessVideo
from run_model import EmotionPredictor  # Replace 'your_module' with the actual module where EmotionPredictor is defined
import datetime

class TestEmotionPredictor(unittest.TestCase):
    def test_load_model(self):
        # Create an instance of EmotionPredictor
        predictor = EmotionPredictor()

        # Verify that the model is loaded correctly
        self.assertIsNotNone(predictor.model)


    def test_predict_emotions(self):
        video_path = "./backend/video/Ses01F_impro01.avi"
        video_preprocessor = PreprocessVideo(video_path=video_path)
        preprocessed_audio_array,corrupted_audio_index = video_preprocessor.get_preprocessed_audio_array()
        audio_duration = video_preprocessor.get_duration()
        emotion_predictor = EmotionPredictor()
        emotion_tags = emotion_predictor.predict_emotions(preprocessed_audio_array,audio_duration,corrupted_audio_index)
        self.assertGreater(len(emotion_tags),0)

        #test to make sure the emotions in emotion_tags are alternating (cannot have 2 of the same emotions consecutive)
        for i in range(len(emotion_tags)-1):
            self.assertNotEqual(emotion_tags[i],emotion_tags[i+1])

        #test if the end time in the last element of emotion_tags is equal to the audio duration
        last_end_time = emotion_tags[-1]['end_time']
        last_end_time = datetime.datetime.strptime(last_end_time, '%H:%M:%S')
        last_end_time = last_end_time.hour*3600 + last_end_time.minute*60 + last_end_time.second
        self.assertEqual(last_end_time,int(audio_duration))


    def test_label_mapping(self):
        label_mapping_df = pd.read_csv('./backend/model/label_mapping.csv')
        label_mapping_dict = dict(zip(label_mapping_df['EncodedLabel'], label_mapping_df['OriginalLabel']))

        test_emotions_array = [0,1,2,3,4,5,6,7,8,9,10,11]
        emotion_tags = [label_mapping_dict[x] for x in test_emotions_array]
        actual_emotions = ['female_angry', 'female_disgust', 'female_fearful','female_happy',
                           'female_neutral','female_sad','male_angry','male_disgust','male_fearful',
                           'male_happy','male_neutral','male_sad']
        self.assertEqual(emotion_tags,actual_emotions)






if __name__ == '__main__':
    unittest.main()
