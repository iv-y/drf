import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/login",
    name: "Login",
    component: () =>
      import("../views/Login.vue")
  },
  {
    path: "/signup",
    name: "Signup",
    component: () =>
      import("../views/Signup.vue")
  },
  {
    path: "/logout",
    name: "Logout",
    component: () =>
      import("../views/Logout.vue")
  },
  {
    path: "/post/:pk",
    name: "Post",
    component: () =>
      import("../views/Post.vue"),
    props: true
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
