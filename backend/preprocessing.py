from moviepy.editor import VideoFileClip
import os
from pydub import AudioSegment
import pandas as pd
import numpy as np
import librosa
from tqdm import tqdm_notebook as tqdm
import scipy.signal
import shutil

class PreprocessVideo:
    def __init__(self,video_path=None,run=True):
        self.video_path = video_path
        self.output_audio_path = None
        self.output_frame_folder = None
        self.preprocessed_audio_array = []
        self.drop_index = []
        self.duration = None
        if run:
            self.run()

    def get_preprocessed_audio_array(self):
        return self.preprocessed_audio_array
    
    def get_duration(self):
        return self.duration
        
    def run(self):
        audio_output_path = "./backend/output/audio.wav"
        frame_output_folder = "./backend/output/audio/frames"

        frame_duration_ms = 3000
        self.extract_audio(self.video_path, audio_output_path)
        self.split_audio_into_frames(audio_output_path, frame_output_folder, frame_duration_ms)
        self.preprocessed_audio_array = self.preprocessing(frame_output_folder)

    def extract_audio(self,video_path, output_audio_path):
        self.output_audio_path = output_audio_path
        #Ensure path exists
        if not os.path.exists(video_path):
            print(f"The video '{video_path}' does not exist.")
            return
        
        # Create the output folder based on give output path
        os.makedirs(os.path.dirname(output_audio_path), exist_ok=True)

        video_clip = VideoFileClip(video_path)
        audio_clip = video_clip.audio
        self.duration = audio_clip.duration
        audio_clip.write_audiofile(output_audio_path)

    def split_audio_into_frames(self,audio_path, output_frame_folder, frame_duration_ms=3000):
        self.output_frame_folder = output_frame_folder
        # Ensure the path exists
        if not os.path.exists(audio_path):
            print(f"The audio '{audio_path}' does not exist.")
            return
        
        audio = AudioSegment.from_file(audio_path)
        # self.clear_directory(output_frame_folder)

        # Create the output folder if it doesn't exist
        os.makedirs(output_frame_folder, exist_ok=True)

        frame_count = 0
        for start_time in range(0, len(audio), frame_duration_ms):
            end_time = start_time + frame_duration_ms
            frame = audio[start_time:end_time]

            frame_count += 1
            frame_filename = os.path.join(output_frame_folder, f"frame_{frame_count}.wav")
            frame.export(frame_filename, format="wav")


    def clear_directory(self,directory_path):
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
                    shutil.rmtree(file_path)
                    # pass
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

        print(f"All files in '{directory_path}' have been deleted.")


    def preprocessing(self,frame_output_folder):
        # Ensure the path exists
        if not os.path.exists(frame_output_folder):
            print(f"The directory '{frame_output_folder}' does not exist.")
            return
        # Initialize an empty list to store audio fragment paths
        audio_paths = []

        # List all files in the output folder
        for filename in os.listdir(frame_output_folder):
            # Check if the file is a WAV file
            if filename.endswith(".wav"):
                # Add the path to the list of audio fragment paths
                audio_paths.append(os.path.join(frame_output_folder, filename))    
        
        # Now, audio_paths contains the paths of all audio fragment files in the folder
        df = pd.DataFrame({'path': audio_paths})

        audio_duration = 3
        sampling_rate = 22050*2
        input_length = sampling_rate * audio_duration
        n_mfcc = 20
        data_sample= np.zeros(input_length)
        MFCC = librosa.feature.mfcc(y=data_sample, sr=sampling_rate, n_mfcc=n_mfcc)

        audios= np.empty(shape=(df.shape[0],128, MFCC.shape[1], 1))

        count=0
        drop_index = []
        for i in tqdm(range(len(df))):
            signal, sample_rate = librosa.load(df.path[i], res_type='kaiser_fast',sr=sampling_rate)
            signal,index = librosa.effects.trim(signal,top_db = 25)
            signal = scipy.signal.wiener(signal)

            if len(signal) > input_length:
                signal = signal[0:input_length]
            elif  input_length > len(signal):
                max_offset = input_length - len(signal)
                signal = np.pad(signal, (0, max_offset), "constant")

            if np.isnan(signal).any():
                drop_index.append(i)

            else:
                melspec = librosa.feature.melspectrogram(signal, sr=sample_rate, n_mels=128,n_fft=2048,hop_length=512)
                logspec = librosa.amplitude_to_db(melspec)
                logspec = np.expand_dims(logspec, axis=-1)
                audios[count,] = logspec
                count+=1
        print("Number of files corrupted: ",len(drop_index))
        return audios,drop_index
    
    def clear_all_directories(self):
        # Ensure the path exists
        if not os.path.exists("./backend/output"):
            print(f"The directory './backend/output' does not exist.")
            return
        if not os.path.exists("./backend/video"):
            print(f"The directory './backend/video' does not exist.")
            return
        self.clear_directory("./backend/output")
        self.clear_directory("./backend/video")

if __name__ == "__main__":

    # video input path
    video_path = "./backend/video/Ses01F_impro01.avi"
    video_preprocessor = PreprocessVideo(video_path=video_path)
    preprocessed_audio_array = video_preprocessor.get_preprocessed_audio_array()
    # print("preprocessed_audio_array",preprocessed_audio_array)
    

