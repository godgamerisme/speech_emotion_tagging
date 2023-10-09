<template>
  <div class="video-player">
    <video ref="videoPlayer" controls autoplay>
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
    getVideoUrl() {
      // Construct the URL for the video based on the videoKey
      const bucketUrl = "https://mcs21fyp.s3.amazonaws.com/";
      return `${bucketUrl}${this.$route.params.videoKey}`;
    },
  },
  mounted() {
    // Expose the videoPlayer instance as a property
    this.$emit("video-player", this.$refs.videoPlayer);
    console.log("Video player mounted");
    console.log(this.videoSrc);
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
