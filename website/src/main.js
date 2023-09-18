import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { initializeApp } from "firebase/app";

const firebaseConfig = {
  apiKey: "AIzaSyDh-OGfaHdr5973ea8hGYJvJlKRkxkMAog",
  authDomain: "fit3162-mcs21-website.firebaseapp.com",
  projectId: "fit3162-mcs21-website",
  storageBucket: "fit3162-mcs21-website.appspot.com",
  messagingSenderId: "368852834211",
  appId: "1:368852834211:web:e011106fcac06b765fac16"
};

initializeApp(firebaseConfig);

const app = createApp(App)
app.use(router)

app.mount('#app')