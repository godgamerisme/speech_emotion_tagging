import unittest
import os
import shutil
import numpy as np

from preprocessing import PreprocessVideo  

class TestPreprocessVideo(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = "./backend/test_output"
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        # Clean up the temporary directory after each test
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    
    def test_extract_audio(self):
        # Black-box test for extract_audio
        video_path = "./backend/video/Ses01F_impro01.avi"
        output_audio_path = os.path.join(self.test_dir, "test_audio.wav")

        # Create an instance of PreprocessVideo
        preprocess_video = PreprocessVideo(video_path,run=False)

        # Call the extract_audio method
        preprocess_video.extract_audio(video_path, output_audio_path)

        # Check if the output audio file exists
        self.assertTrue(os.path.exists(output_audio_path))

    def test_split_audio_into_frames(self):
        # Black-box test for split_audio_into_frames

        video_path = "./backend/video/Ses01F_impro01.avi"
        audio_path = os.path.join(self.test_dir, "test_audio.wav")
        output_frame_folder = os.path.join(self.test_dir, "test_frames")

        # Create an instance of PreprocessVideo
        preprocess_video = PreprocessVideo(video_path,run=False)

        # Call the extract_audio method
        preprocess_video.extract_audio(video_path, audio_path)

        # Call the split_audio_into_frames method
        preprocess_video.split_audio_into_frames(audio_path, output_frame_folder, frame_duration_ms=3000)

        # Check if the output frame folder exists and contains files
        self.assertTrue(os.path.exists(output_frame_folder))
        self.assertGreater(len(os.listdir(output_frame_folder)), 0)

        #White box testing
        #get the duration of the audio
        duration = preprocess_video.get_duration()
        print("duration",duration)
        #check if number of frames procduced = duration/3000
        self.assertEqual(len(os.listdir(output_frame_folder)),int(duration/3)+1)

        

    def test_preprocessing(self):
        # Black-box test for preprocessing

        video_path = "./backend/video/Ses01F_impro01.avi"

        # Create an instance of PreprocessVideo
        preprocess_video = PreprocessVideo(video_path)

        #Check if the preprocessed_audio_array length >0
        self.assertGreater(len(preprocess_video.preprocessed_audio_array),0)



    # Add more test cases for other methods as needed

if __name__ == '__main__':
    unittest.main()
