<template>
  <div class="patient-details">
    <h3>Patient Details</h3>
    <div class="d-flex flex-column mt-3">
      <span><b>Name</b></span>
      <span>{{ session.patient.name }}</span>
    </div>
    <div class="d-flex flex-column mt-3">
      <span><b>Gender</b></span>
      <span>{{ session.patient.gender }}</span>
    </div>
    <div class="d-flex flex-column mt-3">
      <span><b>Age</b></span>
      <span>{{ session.patient.age }}</span>
    </div>
    <div class="d-flex flex-column mt-3">
      <span><b>Appointment Date</b></span>
      <span>{{ session.date.toLocaleDateString("en-UK") }}</span>
    </div>
    <div class="d-flex flex-column mt-3">
      <span><b>Doctor</b></span>
      <span>{{ session.doctor }}</span>
    </div>
  </div>
</template>

<script lang="ts">
import { PropType, defineComponent } from 'vue';
import { Session } from '../models/Session';

export default defineComponent({
  // Add props for patient details
  props: {
    session: Object as PropType<Session>
  },
});
</script>

<style scoped></style>
