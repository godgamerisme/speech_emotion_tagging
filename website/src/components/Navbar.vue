<template>
  <nav>
    <router-link to="/"> Home</router-link> |
    <router-link to="/register"> Register</router-link> |
    <router-link to="/sign-in"> Sign In</router-link> |
    <router-link to="/videos"> All Videos</router-link> |
    <router-link to="/video-player"> Video Player</router-link> |
    <router-link to="/upload"> Upload Page</router-link> |
    <button class="btn" @click="handleSignOut()" v-if="isLoggedIn">
      Sign Out
    </button>
  </nav>
</template>

<script>
export default {
  props: ['isLoggedIn'],
  emits: ['onSignOut'],
  methods: {
    handleSignOut() {
      this.$emit('onSignOut');
    }
  },
};
</script>

<style lang="scss" scoped></style>
