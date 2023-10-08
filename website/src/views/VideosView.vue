<template>
  <div>
    <h2>All Videos</h2>
    <div class="thumbnail-grid">
      <div
        v-for="video in videos"
        :key="video.video_key"
        class="thumbnail-container"
        @click="navigateToVideoPlayer(video.video_key)"
      >
        <img :src="getThumbnailUrl(video.thumbnail_key)" :alt="video.title" class="thumbnail-image" />
        <p>Video Key: {{ video.video_key }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { ref, onMounted } from "vue";

export default {
  methods: {
    navigateToVideoPlayer(videoKey) {
      this.$router.push({ name: 'videoPlayer', params: { videoKey } });
    },
  },
  setup() {
    const videos = ref([]);

    const fetchAllVideos = () => {
      axios.get('http://127.0.0.1:5000/all_videos')
        .then(response => {
          videos.value = response.data;
        })
        .catch(error => {
          console.error('Error fetching videos:', error);
        });
    };

    const getThumbnailUrl = (thumbnailKey) => {
    const bucketUrl = 'https://mcs21fyp.s3.amazonaws.com/';
    const thumbnailUrl = `${bucketUrl}${thumbnailKey}`;

    return thumbnailUrl;
    };


    onMounted(() => {
      fetchAllVideos();
    });

    return {
      videos,
      getThumbnailUrl
    };
  }
};
</script>

<style>
.thumbnail-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* Adjust the number of columns as needed */
  gap: 20px; /* Adjust the gap between thumbnails as needed */
}

.thumbnail-container {
  text-align: center;
}

.thumbnail-image {
  max-width: 500px; /* Maximum width for the image */
  max-height: 300px; /* Maximum height for the image */
  width: auto; /* Ensure the image maintains its aspect ratio */
  height: auto; /* Ensure the image maintains its aspect ratio */
}
</style>
