<template>
  <div class="video-player">
    <video ref="videoPlayer" controls autoplay @timeupdate="updateVideoTime">
      <source :src="videoSrc" type="video/mp4" />
      Your browser does not support the video tag.
    </video>
  </div>
</template>

<script>
export default {
  props: {
    videoSrc: String,
  },
  methods: {
    updateVideoTime() {
      console.log("video time updated!");
      // Emit the video-player event with the updated videoPlayer reference
      this.$emit("video-player", this.$refs.videoPlayer);
    },
  },
  mounted() {
    // Expose the videoPlayer instance as a property
    this.$emit("video-player", this.$refs.videoPlayer);
    console.log("Video player mounted");
    console.log(this.videoSrc);
    this.$refs.videoPlayer.addEventListener("timeupdate", this.updateCurrentEmotion);
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
