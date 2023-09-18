<template>
    <div class="home-container">
      <div class="content">
        <div class="text">
          <h1 class="welcome-text">Welcome Back, Therapist</h1>
        </div>
        <div class="image">
          <img src="@/assets/brain.jpg" alt="Brain" class="brain-image" />
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Home',
  };
  </script>
  
  <style scoped>
  .home-container {
    display: flex;
    justify-content: center; /* Center content horizontally */
    align-items: center; /* Center content vertically */
    height: 80vh; /* Make the container take the full viewport height */
  }
  
  .content {
    display: flex;
    justify-content: space-between; /* Separate content to left and right */
    align-items: center; /* Center content vertically */
    max-width: 800px; /* Set a maximum width for content */
    width: 100%;
    padding: 0 20px; /* Add padding for spacing */
  }
  
  .text {
    flex: 1; /* Expand to fill available space */
    text-align: left;
  }
  
  .welcome-text {
    font-size: 5rem; /* Adjust the font size as needed */
  }
  
  .image {
    flex: 1; /* Expand to fill available space */
    text-align: right;
  }
  
  .brain-image {
    max-width: 450px; /* Set the maximum width for the image */
    height: auto;
  }
  </style>
  