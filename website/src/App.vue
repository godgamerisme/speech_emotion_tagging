<template>
  <nav>
    <router-link to="/"> Home</router-link> |
    <router-link to="/register"> Register</router-link> |
    <router-link to="/sign-in"> Sign In</router-link> |
    <router-link to="/videos"> All Videos</router-link> | 
  </nav>
  <router-view />
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

nav {
  font-size: 25px; /* Adjust the font size as needed */
}

router-link {
  text-decoration: none; /* Remove underline from router-links */
  color: #333; /* Change the color as needed */
  margin: 0 10px; /* Add margin to separate the links */
}

</style>
