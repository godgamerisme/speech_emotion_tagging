<template>
  <div class="container mt-5">
    <div class="d-flex gap-3">
      <video-player
        v-if="videoSrc"
        class="w-75"
        :videoSrc="this.videoSrc"
        @video-player="setVideoPlayer"
      />
      <div class="d-flex flex-column gap-3 w-25">
        <patient-details class="card p-4" :session="session" />
        <patient-emotions
          class="card p-4"
          :emotions="emotions"
          :videoPlayer="videoPlayer"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import VideoPlayer from "./PatientVideo.vue";
import PatientDetails from "./PatientDetails.vue";
import PatientEmotions from "./PatientEmotions.vue";
import axios from "axios";

const domain_url = "http://127.0.0.1:5000";

export default {
  components: {
    VideoPlayer,
    PatientDetails,
    PatientEmotions,
  },
  data() {
    return {
      videoSrc: String,
      videoKey: String,
      session: {
        // date: new Date("2023-10-02"),
        // doctor: "Dr. Smith",
        // patient: {
        //   age: 30,
        //   gender: "Male",
        //   name: "John Doe",
        // },
        date: new Date("2023-10-02"),
        doctor: "Dr. Smith",
        patient: {
          age: 30,
          gender: "Male",
          name: "John Doe",
        },
      },
      emotions2: [
        {
          emotion: "Happy",
          src: "/src/assets/icons/emotions/happy.png",
          start: "00:00",
          end: "01:32",
        },
        {
          emotion: "Sad",
          src: "/src/assets/icons/emotions/sad.png",
          start: "01:32",
          end: "04:01",
        },
        {
          emotion: "Angry",
          src: "/src/assets/icons/emotions/angry.png",
          start: "04:01",
          end: "07:32",
        },
        {
          emotion: "Calm",
          src: "/src/assets/icons/emotions/calm.png",
          start: "07:32",
          end: "08:04",
        },
        // Add more emotion objects with timestamps as needed
      ],
      emotions: [
        {
          begin_time: "0:00:00",
          emotion: "male_disgust",
          end_time: "0:00:03",
        },
        {
          begin_time: "0:00:03",
          emotion: "male_fearful",
          end_time: "0:00:06",
        },
        {
          begin_time: "0:00:06",
          emotion: "male_fearful",
          end_time: "0:00:09",
        },
        {
          begin_time: "0:00:09",
          emotion: "male_fearful",
          end_time: "0:00:12",
        },
        {
          begin_time: "0:00:12",
          emotion: "male_disgust",
          end_time: "0:00:15",
        },
        {
          begin_time: "0:00:15",
          emotion: "male_angry",
          end_time: "0:00:18",
        },
        {
          begin_time: "0:00:18",
          emotion: "male_fearful",
          end_time: "0:00:21",
        },
        {
          begin_time: "0:00:21",
          emotion: "male_happy",
          end_time: "0:00:24",
        },
        {
          begin_time: "0:00:24",
          emotion: "male_fearful",
          end_time: "0:00:27",
        },
        {
          begin_time: "0:00:27",
          emotion: "male_angry",
          end_time: "0:00:30",
        },
        {
          begin_time: "0:00:30",
          emotion: "male_angry",
          end_time: "0:00:33",
        },
        {
          begin_time: "0:00:33",
          emotion: "male_disgust",
          end_time: "0:00:36",
        },
        {
          begin_time: "0:00:36",
          emotion: "male_fearful",
          end_time: "0:00:39",
        },
        {
          begin_time: "0:00:39",
          emotion: "male_disgust",
          end_time: "0:00:42",
        },
        {
          begin_time: "0:00:42",
          emotion: "female_angry",
          end_time: "0:00:45",
        },
        {
          begin_time: "0:00:45",
          emotion: "male_happy",
          end_time: "0:00:48",
        },
        {
          begin_time: "0:00:48",
          emotion: "male_disgust",
          end_time: "0:00:51",
        },
        {
          begin_time: "0:00:51",
          emotion: "female_angry",
          end_time: "0:00:54",
        },
        {
          begin_time: "0:00:54",
          emotion: "male_fearful",
          end_time: "0:00:57",
        },
        {
          begin_time: "0:00:57",
          emotion: "male_happy",
          end_time: "0:01:00",
        },
        {
          begin_time: "0:01:00",
          emotion: "male_fearful",
          end_time: "0:01:03",
        },
        {
          begin_time: "0:01:03",
          emotion: "male_angry",
          end_time: "0:01:06",
        },
        {
          begin_time: "0:01:06",
          emotion: "male_disgust",
          end_time: "0:01:09",
        },
        {
          begin_time: "0:01:09",
          emotion: "male_fearful",
          end_time: "0:01:12",
        },
        {
          begin_time: "0:01:12",
          emotion: "male_sad",
          end_time: "0:01:15",
        },
        {
          begin_time: "0:01:15",
          emotion: "male_angry",
          end_time: "0:01:18",
        },
        {
          begin_time: "0:01:18",
          emotion: "male_disgust",
          end_time: "0:01:21",
        },
        {
          begin_time: "0:01:21",
          emotion: "male_fearful",
          end_time: "0:01:24",
        },
        {
          begin_time: "0:01:24",
          emotion: "male_angry",
          end_time: "0:01:27",
        },
        {
          begin_time: "0:01:27",
          emotion: "male_angry",
          end_time: "0:01:30",
        },
        {
          begin_time: "0:01:30",
          emotion: "male_neutral",
          end_time: "0:01:33",
        },
        {
          begin_time: "0:01:33",
          emotion: "male_disgust",
          end_time: "0:01:36",
        },
        {
          begin_time: "0:01:36",
          emotion: "male_disgust",
          end_time: "0:01:39",
        },
        {
          begin_time: "0:01:39",
          emotion: "male_disgust",
          end_time: "0:01:42",
        },
        {
          begin_time: "0:01:42",
          emotion: "male_disgust",
          end_time: "0:01:45",
        },
        {
          begin_time: "0:01:45",
          emotion: "male_disgust",
          end_time: "0:01:48",
        },
        {
          begin_time: "0:01:48",
          emotion: "male_disgust",
          end_time: "0:01:51",
        },
        {
          begin_time: "0:01:51",
          emotion: "male_angry",
          end_time: "0:01:52",
        },
      ],
      videoPlayer: null,
    };
  },
  mounted() {
    this.videoSrc = "";
    this.videoKey = this.$route.params.videoKey;
    console.log(this.videoKey);
    this.fetchVideoData(this.videoKey);
    this.patientName = "";
    this.age = "";
    this.therapistName = "";
    this.date = "";
    this.emotionTags = null;
  },
  created() {},

  methods: {
    setVideoPlayer(videoPlayer) {
      // Capture the videoPlayer reference
      this.videoPlayer = videoPlayer;
    },
    async fetchVideoData(videoKey) {
      //   console.log(videoKey);

      const url = domain_url + "/get_video";
      const formData = new FormData();
      formData.append("video_key", videoKey);
      const response = await axios
        .post(url, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          //   console.log(response.data);
          this.videoSrc = response.data.url;
          //   this.session = response.data.session;
          //   this.emotions = response.data.emotions;
          //   console.log(this.videoSrc);
          this.session.patient.name = response.data.patientName;
          this.session.patient.age = response.data.age;
          this.session.doctor = response.data.therapistName;
          this.session.date = new Date(response.data.date);
          this.emotionTags = response.data.emotionTags;
        })
        .catch((error) => {
          console.log("Error making POST request: ", error);
        });
    },
  },
};
</script>
