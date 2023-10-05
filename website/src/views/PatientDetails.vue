<template>
    <div class="patient-details">
      <h2>Patient Details</h2>
      <p>Name: {{ patientName }}</p>
      <p>Age: {{ patientAge }}</p>
      <p>Appointment Date: {{ appointmentDate }}</p>
      <p>Doctor: {{ doctorName }}</p>
    </div>
  </template>
  
  <script>
  export default {
    // Add props for patient details
    props: {
      patientName: String,
      patientAge: Number,
      appointmentDate: String,
      doctorName: String,
    },
  };
  </script>
  
  <style scoped>
  .patient-details {
    width: 30%; /* 33% of the screen width */
    float: right;
    background-color: #f0f0f0;
    margin-top: 20px;
    font-size: 18px;
  }
  </style>
  