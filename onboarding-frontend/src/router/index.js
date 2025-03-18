import { createRouter, createWebHistory } from "vue-router";
import HomePage from "@/pages/HomePage.vue";
import UvImpactPage from "@/pages/UvImpactPage.vue";
import ClothAdvicePage from "@/pages/ClothAdvicePage.vue";
import ReminderSetPage from "@/pages/ReminderSetPage.vue";
import Sunscreen_Page from "@/pages/Sunscreen_Page.vue";

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
    path: "/sunscreen",
    name: "sunscreen",
    component: Sunscreen_Page,
  },
  {
    path: "/cloth-advice",
    name: "cloth-advice",
    component: ClothAdvicePage,
  },
  {
    path: "/sunscreen/reminder",
    name: "reminder",
    component: ReminderSetPage,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
