<template>
  <div class="container ml-3 my-4 w-75">
    <div class="form-group">
      <label for="formFile" class="form-label mt-4">Upload Video File</label>
      <input
        class="form-control"
        type="file"
        id="formFile"
        @change="handleFileUpload"
        accept=".mp4,.avi"
      />
    </div>

    <div class="form-group">
      <label for="patientName" class="form-label mt-4">Patient's Name</label>
      <input
        type="text"
        class="form-control"
        id="patientName"
        v-model="patientName"
        placeholder="Enter patient name"
      />
    </div>
    <div class="form-group">
      <label for="therapistName" class="form-label mt-4"
        >Therapist's Name</label
      >
      <input
        type="text"
        class="form-control"
        id="therapistName"
        v-model="therapistName"
        placeholder="Enter therapist name"
      />
    </div>
    <div class="form-group">
      <label for="patientAge" class="form-label mt-4">Patient's Age</label>
      <input
        type="number"
        class="form-control"
        id="patientAge"
        v-model="patientAge"
        placeholder="Enter patient age"
        min="1"
        max="100"
      />
    </div>
    <div class="form-group">
      <label for="selectGender" class="form-label mt-4">Patient's Gender</label>
      <select v-model="patientGender" class="form-select" id="selectGender">
        <option value="Male">Male</option>
        <option value="Female">Female</option>
      </select>
    </div>
    <div class="container mt-4">
      <div class="d-flex justify-content-end">
        <button type="submit" @click="uploadVideo" class="btn btn-primary">
          Upload Video
        </button>
      </div>
    </div>
    <div v-if="alertError" class="alert alert-dismissible alert-danger mt-4">
      <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
      <strong>{{ message }}</strong>
    </div>
    <div
      v-if="uploadSuccess"
      class="alert alert-dismissible alert-success mt-4"
    >
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
      // alertError: false,
      // message: "",
      // uploadSuccess: false,
    };
  },
  created() {
    // Initialize data when the component is created
    // this.resetData();
  },
  methods: {
    // resetData() {
    //   this.patientGender = "";
    //   this.alertError = false;
    //   this.message = "";
    //   this.uploadSuccess = false;
    // },
  },

  setup() {
    const patientName = ref("");
    const therapistName = ref("");
    const patientAge = ref("");
    const patientGender = ref("Male");
    let selectedFile = ref(null);
    let uploadSuccess = ref(false);
    let alertError = ref(false);
    let message = ref("");

    const handleFileUpload = (event) => {
      selectedFile = event.target.files[0];
    };

    const uploadVideo = () => {

      // No File Selected
      if (selectedFile.__v_isRef) {
        alertError.value = true;
        message.value = "Please attach a file before clicking upload";
        return;
      }

      // Invalid File Type Selected
      if (selectedFile.type != "video/mp4" && selectedFile.type != "video/avi") {
        alertError.value = true;
        message.value = "Please upload either an MP4 or AVI File";
        return;
      }

      // Invalid patient name
      if (!patientName.value.trim()) {
        alertError.value = true;
        message.value = "Please enter the patient's name.";
        return;
      }

      // Invalid therapist name
      if (!therapistName.value.trim()) {
        alertError.value = true;
        message.value = "Please enter the therapist's name.";
        return;
      }

      // Invalid age datatype
      if (typeof patientAge.value != "number") {
        alertError.value = true;
        message.value = "Please enter only numbers for Age";
        return;
      }

      // Invalid patient age range
      console.log(typeof patientAge.value != "number")
      if (!patientAge.value || patientAge.value < 13 || patientAge.value > 100) {
        alertError.value = true;
        message.value = "Please enter a valid age between 13 and 100.";
        return;
      }

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
          if (response.status == 200) {
            uploadSuccess.value = true;
            message.value = "Video uploaded successfully";
          }
        })
        .catch((error) => {
          // Handle errors
          console.error("Error uploading video:", error);
          alertError.value = true;
          message.value = "Error uploading video:" + error;
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
      uploadSuccess,
      alertError,
      message,
    };
  },
};
</script>
