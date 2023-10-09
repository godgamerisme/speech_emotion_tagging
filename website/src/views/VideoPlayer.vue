<template>
    <div>
      <video-player :videoSrc="videoSrc" @video-player="setVideoPlayer"/>
      <patient-details
        :patientName="patientName"
        :patientAge="patientAge"
        :appointmentDate="appointmentDate"
        :doctorName="doctorName"
      />
      <patient-emotions :emotions="emotions" :videoPlayer="videoPlayer" />
    </div>
  </template>
  
  <script>
  import VideoPlayer from './PatientVideo.vue';
  import PatientDetails from './PatientDetails.vue';
  import PatientEmotions from './PatientEmotions.vue';
  
  export default {
    props: {
        videoSrc: String,
    },
    components: {
      VideoPlayer,
      PatientDetails,
      PatientEmotions,
    },
    data() {
      return {
        patientName: 'John Doe',
        patientAge: 30,
        appointmentDate: '2023-10-02',
        doctorName: 'Dr. Smith',
        // emotions2: [
        // {
        //       "begin_time": "0:00:00",
        //       "emotion": "male_disgust",
        //       "end_time": "0:00:03"
        //   },
        //   {
        //       "begin_time": "0:00:03",
        //       "emotion": "male_fearful",
        //       "end_time": "0:00:06"
        //   },
        //   {
        //       "begin_time": "0:00:06",
        //       "emotion": "male_neutral",
        //       "end_time": "0:00:09"
        //   },
        //   {
        //       "begin_time": "0:00:09",
        //       "emotion": "male_neutral",
        //       "end_time": "0:00:12"
        //   },
        // ],
        emotions: [
        {
            "begin_time": "0:00:00",
            "emotion": "male_disgust",
            "end_time": "0:00:03"
        },
        {
            "begin_time": "0:00:03",
            "emotion": "male_fearful",
            "end_time": "0:00:06"
        },
        {
            "begin_time": "0:00:06",
            "emotion": "male_fearful",
            "end_time": "0:00:09"
        },
        {
            "begin_time": "0:00:09",
            "emotion": "male_fearful",
            "end_time": "0:00:12"
        },
        {
            "begin_time": "0:00:12",
            "emotion": "male_disgust",
            "end_time": "0:00:15"
        },
        {
            "begin_time": "0:00:15",
            "emotion": "male_angry",
            "end_time": "0:00:18"
        },
        {
            "begin_time": "0:00:18",
            "emotion": "male_fearful",
            "end_time": "0:00:21"
        },
        {
            "begin_time": "0:00:21",
            "emotion": "male_happy",
            "end_time": "0:00:24"
        },
        {
            "begin_time": "0:00:24",
            "emotion": "male_fearful",
            "end_time": "0:00:27"
        },
        {
            "begin_time": "0:00:27",
            "emotion": "male_angry",
            "end_time": "0:00:30"
        },
        {
            "begin_time": "0:00:30",
            "emotion": "male_angry",
            "end_time": "0:00:33"
        },
        {
            "begin_time": "0:00:33",
            "emotion": "male_disgust",
            "end_time": "0:00:36"
        },
        {
            "begin_time": "0:00:36",
            "emotion": "male_fearful",
            "end_time": "0:00:39"
        },
        {
            "begin_time": "0:00:39",
            "emotion": "male_disgust",
            "end_time": "0:00:42"
        },
        {
            "begin_time": "0:00:42",
            "emotion": "female_angry",
            "end_time": "0:00:45"
        },
        {
            "begin_time": "0:00:45",
            "emotion": "male_happy",
            "end_time": "0:00:48"
        },
        {
            "begin_time": "0:00:48",
            "emotion": "male_disgust",
            "end_time": "0:00:51"
        },
        {
            "begin_time": "0:00:51",
            "emotion": "female_angry",
            "end_time": "0:00:54"
        },
        {
            "begin_time": "0:00:54",
            "emotion": "male_fearful",
            "end_time": "0:00:57"
        },
        {
            "begin_time": "0:00:57",
            "emotion": "male_happy",
            "end_time": "0:01:00"
        },
        {
            "begin_time": "0:01:00",
            "emotion": "male_fearful",
            "end_time": "0:01:03"
        },
        {
            "begin_time": "0:01:03",
            "emotion": "male_angry",
            "end_time": "0:01:06"
        },
        {
            "begin_time": "0:01:06",
            "emotion": "male_disgust",
            "end_time": "0:01:09"
        },
        {
            "begin_time": "0:01:09",
            "emotion": "male_fearful",
            "end_time": "0:01:12"
        },
        {
            "begin_time": "0:01:12",
            "emotion": "male_sad",
            "end_time": "0:01:15"
        },
        {
            "begin_time": "0:01:15",
            "emotion": "male_angry",
            "end_time": "0:01:18"
        },
        {
            "begin_time": "0:01:18",
            "emotion": "male_disgust",
            "end_time": "0:01:21"
        },
        {
            "begin_time": "0:01:21",
            "emotion": "male_fearful",
            "end_time": "0:01:24"
        },
        {
            "begin_time": "0:01:24",
            "emotion": "male_angry",
            "end_time": "0:01:27"
        },
        {
            "begin_time": "0:01:27",
            "emotion": "male_angry",
            "end_time": "0:01:30"
        },
        {
            "begin_time": "0:01:30",
            "emotion": "male_neutral",
            "end_time": "0:01:33"
        },
        {
            "begin_time": "0:01:33",
            "emotion": "male_disgust",
            "end_time": "0:01:36"
        },
        {
            "begin_time": "0:01:36",
            "emotion": "male_disgust",
            "end_time": "0:01:39"
        },
        {
            "begin_time": "0:01:39",
            "emotion": "male_disgust",
            "end_time": "0:01:42"
        },
        {
            "begin_time": "0:01:42",
            "emotion": "male_disgust",
            "end_time": "0:01:45"
        },
        {
            "begin_time": "0:01:45",
            "emotion": "male_disgust",
            "end_time": "0:01:48"
        },
        {
            "begin_time": "0:01:48",
            "emotion": "male_disgust",
            "end_time": "0:01:51"
        },
        {
            "begin_time": "0:01:51",
            "emotion": "male_angry",
            "end_time": "0:01:52"
        }
    ],
        videoPlayer: null, // Initialize videoPlayer as null
      };
    },
    methods: {
    setVideoPlayer(videoPlayer) {
      // Capture the videoPlayer reference
      this.videoPlayer = videoPlayer;
    },
  },
};
  </script>
  