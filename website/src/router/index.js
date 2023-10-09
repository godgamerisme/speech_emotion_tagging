import { createRouter, createWebHistory } from "vue-router";
import { getAuth, onAuthStateChanged } from "firebase/auth";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/home", component: () => import("../views/HomeView.vue") },
    { path: "/register", component: () => import("../views/RegisterView.vue") },
    { path: "/", component: () => import("../views/SignInView.vue") },
    {
      path: "/videos",
      component: () => import("../views/VideosView.vue"),
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: "/video-player",
      component: () => import("../views/VideoPlayer.vue"),
    },
    { path: "/upload", component: () => import("../views/UploadView.vue") },
  ],
});

const getCurrentUser = () => {
  return new Promise((resolve, reject) => {
    const removeListener = onAuthStateChanged(
      getAuth(),
      (user) => {
        removeListener();
        resolve(user);
      },
      reject
    );
  });
};

router.beforeEach(async (to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (await getCurrentUser) {
      next();
    } else {
      alert("you do not have access!");
      next("/");
    }
  } else {
    next();
  }
});

export default router;
