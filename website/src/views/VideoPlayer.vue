<template>
  <div class="container mt-5">
    <div class="d-flex gap-3">
      <video-player class="w-75" :videoSrc="videoSrc" />
      <div class="d-flex flex-column gap-3 w-25">
        <patient-details
          class="card p-4"
          :patientName="patientName"
          :patientAge="patientAge"
          :appointmentDate="appointmentDate"
          :doctorName="doctorName"
        />
        <patient-emotions class="card p-4" :emotions="emotions" />
      </div>
    </div>
  </div>
</template>

<script>
import VideoPlayer from "./PatientVideo.vue";
import PatientDetails from "./PatientDetails.vue";
import PatientEmotions from "./PatientEmotions.vue";

export default {
  components: {
    VideoPlayer,
    PatientDetails,
    PatientEmotions,
  },
  data() {
    return {
      videoSrc: "path/to/your/video.mp4",
      patientName: "John Doe",
      patientAge: 30,
      appointmentDate: "2023-10-02",
      doctorName: "Dr. Smith",
      emotions: [
        { emotion: "Happy", start: "00:00", end: "00:50" },
        // Add more emotion objects with timestamps as needed
      ],
    };
  },
};
</script>
