<!-- All Videos Part 1-->
<template>
    <div class="container">
      <div class="video">
        <h2 class="video-title">All Videos</h2>
        <div class="video-content">
          <p class="video-description">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eget lectus id libero ultricies dapibus. Fusce sit amet est nec ex convallis interdum.
          </p>
        </div>
        <img src="@/assets/video.jpg" alt="Video Placeholder" class="video-image" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Videos',
  };
  </script>
  
  <style scoped>
  .container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .video {
    display: flex;
    flex-direction: column; /* Stack elements vertically */
    align-items: center; /* Center elements horizontally */
    text-align: center; /* Center text */
    margin-bottom: 20px;
  }
  
  .video-title {
    font-size: 2rem; /* Increase title font size */
    margin-bottom: 10px;
  }
  
  .video-content {
    text-align: left; /* Align text on the left */
    margin-bottom: 20px; /* Add margin for spacing */
  }
  
  .video-description {
    font-size: 1.2rem; /* Increase text font size */
  }
  
  .video-image {
    max-width: 100%; /* Make the video image full width */
    height: auto;
  }
  </style>
  

  <!-- All Videos Part 1-->
  <template>
    <div>
      <h2>All Videos</h2>
      <p> Hello</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    setup() {
      const handleGet = () => {
      // Fetch all videos from your backend API
      axios.get('http://127.0.0.1:5000/all_videos')
        .then(response => {
          console.log("all got")
        })
        .catch(error => {
          console.error('Error fetching videos:', error);
        });
    };
  
    return {
      handleGet
    };
  },
  };
  </script>
  
  <style scoped>
  .video-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
  }
  
  .video-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  
  .metadata {
    margin-top: 10px;
  }
  </style>
  