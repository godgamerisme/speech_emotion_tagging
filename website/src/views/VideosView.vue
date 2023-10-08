<template>
  <div>
    <h2>All Videos</h2>
    <ul>
      <li
        v-for="video in videos"
        :key="video.video_key"
        @onClick="sendToPatientVideo"
      >
        Video Key: {{ video.video_key }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";
import { ref, onMounted } from "vue";

export default {
  setup() {
    const videos = ref([]);

    const fetchAllVideos = () => {
      axios
        .get("http://127.0.0.1:5000/all_videos")
        .then((response) => {
          videos.value = response.data;
        })
        .catch((error) => {
          console.error("Error fetching videos:", error);
        });
    };

    onMounted(() => {
      fetchAllVideos();
    });

    return {
      videos,
    };
  },
};
</script>
