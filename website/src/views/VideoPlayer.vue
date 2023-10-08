<template>
    <div>
      <video-player :videoSrc="videoSrc" />
      <patient-details
        :patientName="patientName"
        :patientAge="patientAge"
        :appointmentDate="appointmentDate"
        :doctorName="doctorName"
      />
      <patient-emotions :emotions="emotions" />
    </div>
  </template>
  
  <script>
  import VideoPlayer from './PatientVideo.vue';
  import PatientDetails from './PatientDetails.vue';
  import PatientEmotions from './PatientEmotions.vue';
  
  export default {
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
        emotions: [
          { emotion: 'Happy ', start: '00:00', end: '00:50' },
          // Add more emotion objects with timestamps as needed
        ],
      };
    },
  };
  </script>
  