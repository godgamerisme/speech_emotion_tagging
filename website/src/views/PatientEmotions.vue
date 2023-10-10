<template>
  <div class="patient-emotions">
    <h3>Patient Emotions</h3>
    <div
      v-for="(emotionType, emotionsOfType) in emotionsGrouped"
      :key="emotionType"
    >
      <h3 @click="playAll(emotionType)" class="mt-3">
        <i v-if="emotionsOfType==='male_fearful'" class="fa-regular fa-face-frown-open"></i>
        <i v-else-if="emotionsOfType==='male_sad'" class="fa-regular fa-face-frown"></i> 
        <i v-else-if="emotionsOfType==='male_happy'" class="fa-regular fa-face-smile"></i> 
        <i v-else-if="emotionsOfType==='male_disgust'" class="fa-regular fa-face-tired"></i>
        <i v-else-if="emotionsOfType==='male_neutral'" class="fa-regular fa-face-meh"></i>  
        <i v-else-if="emotionsOfType==='male_angry'" class="fa-regular fa-face-angry"></i>    
        {{ emotionsOfType }}</h3>
      <ul>
        <li
          v-for="(emotion, index) in emotionType"
          :key="index"
          @click="seekToEmotion(emotion)"
          class="d-flex flex-row mt-3 align-items-center gap-3"
        >
          <!-- <img class="w-20" :src="emotion.src" :alt="emotion.emotion"> -->
          <div class="d-flex flex-column">
            <span
              ><b>{{ emotion.emotion }}</b></span
            >
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
    console.log("emotions", this.emotions);
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
      const [hours, minutes, seconds] = time.split(":").map(Number);
      return hours * 3600 + minutes * 60 + seconds;
    },
    async playAll(emotionType) {
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
        const duration =
          this.convertTimeToSeconds(emotion.end_time) - startTime + 1;
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
ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
</style>
