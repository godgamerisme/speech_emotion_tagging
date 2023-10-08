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
  </style>
  