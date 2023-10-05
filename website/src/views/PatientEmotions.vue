<template>
  <div class="patient-emotions">
    <h2>Patient Emotions</h2>
    <ul>
      <li v-for="(emotion, index) in emotions" :key="index" @click="navigateToTime(emotion.start, emotion.end)">
        <div>
          <span>{{ emotion.emotion &nbsp;}} </span>
          <span>{{ (emotion.start) }} - {{ (emotion.end) }}</span>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    emotions: Array, // An array of emotion objects with start and end times
  },
  methods: {
    navigateToTime(startTime, endTime) {
      // Implement logic to navigate to the specific time range in the video
      // You can use JavaScript's currentTime property to set the video playback time
      // For example, if you have a reference to the video element, you can do:
      // this.$refs.videoPlayer.currentTime = parseTimestamp(startTime);
      // Also, you can set the endTime if needed.
    },
    formatTime(timestamp) {
      // Implement a function to format the timestamp (e.g., convert seconds to HH:MM:SS)
      // Example:
      // const time = new Date(timestamp * 1000).toISOString().substr(11, 8);
      // return time;
    },
  },
};
</script>

<style scoped>
.patient-emotions {
  width: 30%; /* 30% of the screen width */
  float: right;
  background-color: #f0f0f0;
  margin-top: 20px;
  font-size: 18px;
  cursor: pointer; /* Change cursor to pointer for clickable elements */
}
</style>
