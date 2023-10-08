<template>
  <div class="container mt-5">
    <div class="d-flex gap-3">
      <video-player class="w-75" :videoSrc="videoSrc" />
      <div class="d-flex flex-column gap-3 w-25">
        <patient-details
          class="card p-4"
          :session="session"
        />
        <patient-emotions class="card p-4" :emotions="emotions" />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import VideoPlayer from "./PatientVideo.vue";
import PatientDetails from "./PatientDetails.vue";
import PatientEmotions from "./PatientEmotions.vue";
import { Session } from "../models/Session";

export default {
  components: {
    VideoPlayer,
    PatientDetails,
    PatientEmotions,
  },
  data() {
    return {
      session: {
        date: new Date("2023-10-02"),
        doctor: "Dr. Smith",
        patient: {
          age: 30,
          gender: "Male",
          name: "John Doe"
        }
      },
      videoSrc: "path/to/your/video.mp4",
      // patientName: "John Doe",
      // patientAge: 30,
      // appointmentDate: "2023-10-02",
      // doctorName: "Dr. Smith",
      emotions: [
        { emotion: "Happy", src: "/src/assets/icons/emotions/happy.png", start: "00:00", end: "01:32" },
        { emotion: "Sad", src: "/src/assets/icons/emotions/sad.png", start: "01:32", end: "04:01" },
        { emotion: "Angry", src: "/src/assets/icons/emotions/angry.png", start: "04:01", end: "07:32" },
        { emotion: "Calm", src: "/src/assets/icons/emotions/calm.png", start: "07:32", end: "08:04" },
        // Add more emotion objects with timestamps as needed
      ],
    };
  },
};
</script>
