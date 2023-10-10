<template>
  <nav class="navbar navbar-expand-lg bg-dark" data-bs-theme="dark">
    <!-- <div class="container-fluid" bis_skin_checked="1"> -->
    <!-- <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarColor02"
        aria-controls="navbarColor02"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button> -->
    <div
      class="collapse navbar-collapse"
      id="navbarColor02"
      bis_skin_checked="1"
    >
      <ul class="navbar-nav me-auto" v-if="isLoggedIn">
        <li class="nav-item">
          <router-link class="nav-link active" to="/home"
            >Home
            <span class="visually-hidden">(current)</span>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" to="/videos">All Videos</router-link>
        </li>
        <!-- <li class="nav-item">
            <router-link class="nav-link" to="/video-player"
              >Video Player</router-link
            >
          </li> -->
        <li class="nav-item">
          <router-link class="nav-link" to="/upload">Upload Page</router-link>
        </li>
      </ul>
    </div>
    <div class="d-flex gap-2">
      <button
        v-if="isLoggedIn"
        @click="handleSignOut()"
        class="btn btn-primary"
      >
        Sign Out
      </button>
      <router-link v-else to="/" class="btn btn-primary">Sign In</router-link>
      <router-link v-if="!isLoggedIn" to="/register" class="btn btn-secondary"
        >Register</router-link
      >
    </div>
    <!-- </div> -->
  </nav>
</template>

<script>
export default {
  props: ["isLoggedIn"],
  emits: ["onSignOut"],
  methods: {
    handleSignOut() {
      this.$emit("onSignOut");
    },
  },
};
</script>

<style lang="scss" scoped></style>
