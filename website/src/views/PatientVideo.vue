<template>
  <div class="video-player">
    <video ref="videoPlayer" controls>
      <source :src="videoSrc" type="video/mp4" />
      Your browser does not support the video tag.
    </video>
  </div>
</template>

<script>
export default {
  data() {
    return {
      videoSrc: require('@/assets/therapy.mp4'), // Use a relative path to the video file
    };
  },
};
</script>

<style scoped></style>
