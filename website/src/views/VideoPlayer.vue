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
          v-if="emotions.length"
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

      emotions: [],
      videoPlayer: null,
      loaded: false,
    };
  },
  mounted() {
    this.videoSrc = "";
    this.videoKey = this.$route.params.videoKey;
    console.log(this.videoKey);
    this.fetchVideoData(this.videoKey);
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
          this.session.patient.gender = response.data.gender;
          this.session.doctor = response.data.therapistName;
          this.session.date = new Date(response.data.date);
          this.emotions = response.data.emotionTags;
        })
        .catch((error) => {
          console.log("Error making POST request: ", error);
        });
    },
  },
};
</script>
