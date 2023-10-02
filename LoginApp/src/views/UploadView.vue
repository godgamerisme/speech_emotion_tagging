<template>
    <div>
      <input type="file" @change="handleFileUpload" accept=".mp4,.pdf"/>  <!--rmb change this back-->>
      <input type="text" v-model="patientName" placeholder="Enter patient name" />
      <input type="text" v-model="therapistName" placeholder="Enter therapist name" />
      <button @click="uploadVideo">Upload Video</button>
    </div>
  </template>


<script>
import axios from 'axios';
import { ref } from "vue";

export default {
    setup() {
      const patientName = ref('');
      const therapistName = ref('');
      let selectedFile = ref(null);

      const handleFileUpload = (event) => {
      selectedFile = event.target.files[0];
      };

      const uploadVideo = () => {
        const formData = new FormData();
        formData.append('video', selectedFile);
        formData.append('patient_name', patientName.value);
        formData.append('therapist_name', therapistName.value);

        // Make a POST request to your backend API
        axios.post('http://127.0.0.1:5000/upload_video', formData, {
            headers: {
              'Content-Type': 'multipart/form-data',
            },
          })
          .then(response => {
            // Handle the response from the backend
            console.log('Video uploaded successfully');
          })
          .catch(error => {
            // Handle errors
            console.error('Error uploading video:', error);
          });
    };

    return {
        patientName,
        therapistName,
        selectedFile,
        handleFileUpload,
        uploadVideo,
    };
  },
};

</script>

