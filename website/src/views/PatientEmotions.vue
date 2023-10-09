<template>
  <div class="patient-emotions">
    <h2>Patient Emotions</h2>
    <div v-for="(emotionType, emotionsOfType) in emotionsGrouped" :key="emotionType">
      <h3>{{ emotionsOfType }} <button @click="playAll(emotionType)"> Play All </button></h3>
      <ul>
        <li v-for="(emotion, index) in emotionType" :key="index" @click="seekToEmotion(emotion)">
          <div>
            <span>{{ emotion.emotion }}</span>
            <span> ‎ </span>
            <span>{{ emotion.begin_time }} - {{ emotion.end_time }}</span>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    emotions: Array, // An array of emotion objects with start and end times
    videoPlayer: Object,
  },
  data() {
    return {
      emotionTags: [],
    };
  },
  computed: {
    emotionsGrouped() {
      // Group emotions by their emotion type
      const groupedEmotions = {};
      for (const emotion of this.emotionTags) {
        const emotionType = emotion.emotion;
        if (!groupedEmotions[emotionType]) {
          groupedEmotions[emotionType] = [];
        }
        groupedEmotions[emotionType].push(emotion);
      }
      console.log(groupedEmotions);
      return groupedEmotions;
    },
  },
  mounted() {
    this.emotionTags = this.emotions;
  },
  methods: {
    logtoconsole(message) {
      console.log(message);
    },
    seekToEmotion(emotion) {
      // Use the videoPlayer reference to seek to the emotion's start time
      if (this.videoPlayer) {
        const startTime = this.convertTimeToSeconds(emotion.begin_time);
        this.videoPlayer.currentTime = startTime;
      }
    },
    convertTimeToSeconds(time) {
      // Convert time in the format "hh:mm:ss" to seconds
      const [hours, minutes, seconds] = time.split(':').map(Number);
      return hours * 3600 + minutes * 60 + seconds;
    },
    async playAll(emotionType) {
      const emotionsToPlay = this.emotionsGrouped[emotionType];
      if (emotionType && emotionType.length > 0) {
        for (const emotion of emotionType) {
          console.log(emotion);
          await this.playEmotion(emotion);
        }
      }
    },
    playEmotion(emotion) {
      return new Promise((resolve) => {
        const startTime = this.convertTimeToSeconds(emotion.begin_time);
        this.videoPlayer.currentTime = startTime;
        this.videoPlayer.play();
        const duration = this.convertTimeToSeconds(emotion.end_time) - startTime;
        setTimeout(() => {
          this.videoPlayer.pause();
          resolve();
        }, duration * 1000);
      });
    },
  },
};
</script>

<style scoped>
.patient-emotions {
  width: 30%; /* 30% of the screen width */
  float: right;
  background-color: #f0f0f0;
  margin-top: 20px;
  font-size: 18px;
  cursor: pointer; /* Change cursor to pointer for clickable elements */
}
</style>
