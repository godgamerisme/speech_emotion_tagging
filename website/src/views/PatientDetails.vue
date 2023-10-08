<template>
    <div class="patient-details">
      <h3>Patient Details</h3>
      <div class="d-flex flex-column mt-3">
        <span><b>Name</b></span>
        <span>{{ patientName }}</span>
      </div>
      <div class="d-flex flex-column mt-3">
        <span><b>Age</b></span>
        <span>{{ patientAge }}</span>
      </div>
      <div class="d-flex flex-column mt-3">
        <span><b>Appointment Date</b></span>
        <span>{{ appointmentDate }}</span>
      </div>
      <div class="d-flex flex-column mt-3">
        <span><b>Doctor</b></span>
        <span>{{ doctorName }}</span>
      </div>
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
  