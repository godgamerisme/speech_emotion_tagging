<template>
  <div>
    <input type="file" @change="handleFileUpload" accept=".mp4,.avi" />
    <!--rmb change this back-->>
    <input type="text" v-model="patientName" placeholder="Enter patient name" />
    <input
      type="text"
      v-model="therapistName"
      placeholder="Enter therapist name"
    />
    <input type="text" v-model="patientAge" placeholder="Enter patient age" />
    <select v-model="patientGender" placeholder="Select patient gender">
      <option value="Male">Male</option>
      <option value="Female">Female</option>
    </select>
    <button @click="uploadVideo">Upload Video</button>
  </div>

  <div>
    <div v-if="alertError" class="alert alert-dismissible alert-danger">
      <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
      <strong>{{ message }}</strong>
    </div>
    <div v-if="uploadSuccess" class="alert alert-dismissible alert-success">
      <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
      <strong>{{ message }}</strong>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { ref } from "vue";

export default {
  data() {
    return {
      patientGender: "",
      alertError: false,
      message: "",
      uploadSuccess: false,
    };
  },
  created() {
    // Initialize data when the component is created
    this.resetData();
  },
  methods: {
    resetData() {
      this.patientGender = "";
      this.alertError = false;
      this.message = "";
      this.uploadSuccess = false;
    },
  },

  setup() {
    const patientName = ref("");
    const therapistName = ref("");
    const patientAge = ref("");
    const patientGender = ref("Male");
    let selectedFile = ref(null);

    const handleFileUpload = (event) => {
      selectedFile = event.target.files[0];
    };

    const uploadVideo = () => {
      const formData = new FormData();
      formData.append("video", selectedFile);
      formData.append("patient_name", patientName.value);
      formData.append("therapist_name", therapistName.value);
      formData.append("age", patientAge.value);
      formData.append("gender", patientGender.value);

      // Make a POST request to your backend API
      axios
        .post("http://127.0.0.1:5000/upload_video", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          // Handle the response from the backend
          console.log("Video uploaded successfully");
          this.uploadSuccess = true;
          this.message = "Video uploaded successfully";
        })
        .catch((error) => {
          // Handle errors
          console.error("Error uploading video:", error);
          this.alertError = true;
          this.errorMessage = "Error uploading video:" + error;
        });
    };

    return {
      patientName,
      therapistName,
      patientAge,
      patientGender,
      selectedFile,
      handleFileUpload,
      uploadVideo,
    };
  },
};
</script>
