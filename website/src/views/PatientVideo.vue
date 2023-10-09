<template>
  <div class="video-player">
    <video ref="videoPlayer" controls autoplay>
      <source :src="getVideoUrl()">
      Your browser does not support the video tag.
    </video>
  </div>
</template>
  
  <script>
  export default {
    methods: {
      getVideoUrl() {
        // Construct the URL for the video based on the videoKey
        const bucketUrl = 'https://mcs21fyp.s3.amazonaws.com/';
        return `${bucketUrl}${this.$route.params.videoKey}`;
      },
    },
    mounted() {
      // Expose the videoPlayer instance as a property
      this.$emit('video-player', this.$refs.videoPlayer);
    }
  };
  </script>
  
  <style scoped>
  .video-player {
    width: 66%; /* 66% of the screen width */
    float: left;
    margin-top: 20px;
  }
  </style>