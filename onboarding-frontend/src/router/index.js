import { createRouter, createWebHistory } from "vue-router";
import HomePage from "@/pages/HomePage.vue";
import UvImpactPage from "@/pages/UvImpactPage.vue";
import ClothAdvicePage from "@/pages/ClothAdvicePage.vue";
import SunScreenPage from "@/pages/SunScreenPage.vue";
import ReminderPage from "@/pages/ReminderPage.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomePage,
  },
  {
    path: "/uv-impact",
    name: "uv-impact",
    component: UvImpactPage,
  },
  {
    path: "/sun-screen",
    name: "sun-screen",
    component: SunScreenPage,
  },
  {
    path: "/cloth-advice",
    name: "cloth-advice",
    component: ClothAdvicePage,
  },
  {
    path: "/reminder",
    name: "reminder",
    component: ReminderPage,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
