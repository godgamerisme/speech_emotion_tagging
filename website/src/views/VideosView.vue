<template>
  <div>
    <div class="container mt-5">
      <div class="row">
        <!-- Multi-criteria filtering options (left column) -->
        <div class="col-md-3 mt-5 offset-md-1">
          <div class="container border border-primary rounded py-4 pb-5">
            <p class="text-primary fs-2 mb-4">Filters</p>
            <!-- Search bar -->
            <label>Search patient:</label>
            <input
              v-model="searchQuery"
              placeholder="Search by patient name"
              class="form-control"
            />

            <!-- Sorting criteria -->
            <div>
              <label for="sortCriteria" class="mt-4">Sort by:</label>
              <select
                id="sortCriteria"
                v-model="sortCriteria"
                class="form-select my-1"
              >
                <option value="None">None</option>
                <option value="Date">Date</option>
                <option value="Age">Age</option>
              </select>
              <!-- Toggle button for sorting order -->
              <button
                v-if="sortCriteria !== 'None'"
                @click="toggleSortOrder"
                class="btn btn-primary my-1"
              >
                {{ sortOrder === "ascending" ? "Descending" : "Ascending" }}
              </button>
            </div>
          </div>
        </div>
        <!-- Thumbnail grid -->
        <div class="col-md-8">
          <div class="thumbnail-grid">
            <div
              v-for="video in filteredVideos"
              :key="video.video_key"
              class="thumbnail-container"
              @click="navigateToVideoPlayer(video.video_key)"
            >
              <img
                :src="getThumbnailUrl(video.thumbnail_key)"
                :alt="video.metadata.patientName"
                class="thumbnail-image"
              />
              <!-- <p class="m-0">Video Key: {{ video.video_key }}</p> -->
              <p class="m-0">Patient Name: {{ video.metadata.patientName }}</p>
              <p class="m-0">Age: {{ video.metadata.age }}</p>
              <p class="m-0">Date: {{ video.metadata.date }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { ref, onMounted, computed } from "vue";

export default {
  methods: {
    navigateToVideoPlayer(videoKey) {
      this.$router.push({ name: "videoPlayer", params: { videoKey } });
    },
  },
  setup() {
    const videos = ref([]);
    const searchQuery = ref("");
    const sortCriteria = ref("None"); // Default sorting criteria
    const sortOrder = ref("ascending"); // Default sorting order

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

    const getThumbnailUrl = (thumbnailKey) => {
      const bucketUrl = "https://mcs21fyp.s3.amazonaws.com/";
      const thumbnailUrl = `${bucketUrl}${thumbnailKey}`;
      return thumbnailUrl;
    };

    const toggleSortOrder = () => {
      console.log("HERE!");
      sortOrder.value =
        sortOrder.value === "ascending" ? "descending" : "ascending";
    };

    onMounted(() => {
      fetchAllVideos();
    });

    // Create a computed property to filter videos based on searchQuery and sortCriteria
    const filteredVideos = computed(() => {
      let filtered = videos.value.filter((video) =>
        video.metadata.patientName
          .toLowerCase()
          .includes(searchQuery.value.toLowerCase())
      );

      if (sortCriteria.value === "Date") {
        filtered = filtered.sort((a, b) => {
          const dateA = new Date(a.metadata.date);
          const dateB = new Date(b.metadata.date);

          if (sortOrder.value === "ascending") {
            return dateB - dateA;
          } else {
            return dateA - dateB;
          }
        });
      } else if (sortCriteria.value === "Age") {
        // Added sorting by age
        filtered = filtered.sort((a, b) => {
          if (sortOrder.value === "ascending") {
            return b.metadata.age - a.metadata.age;
          } else {
            return a.metadata.age - b.metadata.age;
          }
        });
      }

      return filtered;
    });

    return {
      videos,
      searchQuery,
      sortCriteria,
      sortOrder,
      filteredVideos,
      getThumbnailUrl,
      toggleSortOrder,
    };
  },
};
</script>

<style>
.thumbnail-grid {
  display: grid;
  grid-template-columns: repeat(
    2,
    1fr
  ); /* Adjust the number of columns as needed */
  gap: 20px; /* Adjust the gap between thumbnails as needed */
  max-width: 80%; /* Adjust as needed */
  margin: 0 auto; /* Center the grid horizontally */
}

.thumbnail-container {
  text-align: left;
}

.thumbnail-image {
  max-width: 300px; /* Maximum width for the image */
  max-height: 200px; /* Maximum height for the image */
  width: auto; /* Ensure the image maintains its aspect ratio */
  height: auto; /* Ensure the image maintains its aspect ratio */
}
</style>
