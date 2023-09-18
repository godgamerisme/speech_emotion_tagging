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
  