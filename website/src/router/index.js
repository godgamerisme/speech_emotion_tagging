import { createRouter, createWebHistory } from "vue-router";
import { getAuth, onAuthStateChanged } from "firebase/auth";

const authGuard = async (to, from, next) => {
  const requiresAuth = to.matched.some((record) => record.meta.requiresAuth);

  if (requiresAuth && !(await getCurrentUser())) {
    // Redirect to login if authentication is required but the user is not logged in
    next("/");
  } else {
    // Continue with the navigation
    next();
  }
};

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/home",
      component: () => import("../views/HomeView.vue"),
      meta: { requiresAuth: true },
      beforeEnter: authGuard,
    },
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
      path: "/video-player/:videoKey",
      name: "videoPlayer", // Add a name to the route
      component: () => import("../views/VideoPlayer.vue"),
      meta: { requiresAuth: true },
      beforeEnter: authGuard,
    },
    {
      path: "/upload",
      component: () => import("../views/UploadView.vue"),
      meta: { requiresAuth: true },
      beforeEnter: authGuard,
    },
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

router.beforeEach(authGuard);

export default router;
