<template>
  <div class="video-player">
    <video ref="videoPlayer" controls>
      <source
        src="https://mcs21fyp.s3.amazonaws.com/arman-cf772804-bdfb-41f1-82c7-cbcbc014cb4a?AWSAccessKeyId=AKIATAMTMUSJYTFN2B2F&Signature=4I53%2BelSuDHj1QwsOfJk%2F%2FI6ei0%3D&Expires=1696778124"
      />
      Your browser does not support the video tag.
    </video>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // videoSrc: require('@/assets/therapy.mp4'), // Use a relative path to the video file
    };
  },
};
</script>

<style scoped>
video {
  width: 100%;
  overflow: hidden;
  border-radius: 0.4em;
}
</style>
