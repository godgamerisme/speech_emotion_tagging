<template>
    <div>
      <h2>All Videos</h2>
      <input
        v-model="searchQuery"
        placeholder="Search videos by name"
      />
      <div>
        <button @click="sortVideos('asc')">Sort by Date Ascending</button>
        <button @click="sortVideos('desc')">Sort by Date Descending</button>
      </div>
      <div class="thumbnail-grid">
        <div
          v-for="video in filteredVideos"
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
  import { ref, onMounted, computed } from "vue";
  
  export default {
    // data() {
    //   return {
    //     searchTerm: "", // Initialize the search term
    //   };
    // },
  
    // computed: {
    //   filteredVideos() {
    //     // Use the computed property to filter videos based on the search term
    //     return this.videos.filter((video) =>
    //       video.name.toLowerCase().includes(this.searchTerm.toLowerCase())
    //     );
    //   },
    // },
    
    methods: {
      navigateToVideoPlayer(videoKey) {
        this.$router.push({ name: 'videoPlayer', params: { videoKey } });
      },
      sortAndFilterVideos(order){
        const query = this.searchQuery.toLowerCase();
        const sortedVideos = [...this.videos]; // Clone the videos array
  
        sortedVideos.sort((a, b) => {
          const dateA = new Date(a.metadata.date);
          const dateB = new Date(b.metadata.date);
  
          if (order === 'asc') {
            return dateA - dateB;
          } else if (order === 'desc') {
            return dateB - dateA;
          }
        });
  
        return sortedVideos.filter(video => video.name.toLowerCase().includes(query));
      }
    },
    setup() {
      const videos = ref([]);
      const searchQuery = ref(''); 
      const sortBy = ref('asc'); // Default sorting order
  
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
  
      // // Create a computed property to filter videos based on searchQuery
      // const filteredVideos = computed(() => {
      //   const sortedVideos = [...filteredVideos.value]; // Clone the filtered array
      //   if (sortBy.value === 'asc') {
      //     sortedVideos.sort((a, b) => new Date(a.metadata.date) - new Date(b.metadata.date));
      //   } else if (sortBy.value === 'desc') {
      //     sortedVideos.sort((a, b) => new Date(b.metadata.date) - new Date(a.metadata.date));
      //   }
      //   return sortedVideos;
      // });
      
      return {
        videos,
        getThumbnailUrl,
        // filteredVideos,
        searchQuery,
        sortBy,
        sortAndFilterVideos,
      };
    }
  };
  </script>
  
  <style>
  .thumbnail-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr); /* Adjust the number of columns as needed */
    gap: 20px; /* Adjust the gap between thumbnails as needed */
    max-width: 30%; /* Adjust as needed */
    margin: 0 auto; /* Center the grid horizontally */
  }
  
  .thumbnail-container {
    text-align: center;
  }
  
  .thumbnail-image {
    max-width: 300px; /* Maximum width for the image */
    max-height: 200px; /* Maximum height for the image */
    width: auto; /* Ensure the image maintains its aspect ratio */
    height: auto; /* Ensure the image maintains its aspect ratio */
  }
  </style>