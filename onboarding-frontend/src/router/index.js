import { createRouter, createWebHistory } from "vue-router";
import HomePage from "@/pages/HomePage.vue";
import UvImpactPage from "@/pages/UvImpactPage.vue";
import ClothAdvicePage from "@/pages/ClothAdvicePage.vue";
import Sunscreen_Page from "@/pages/Sunscreen_Page.vue";
import SkinTonePage from "@/pages/SkinTonePage.vue";

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
    path: "/skin-tone",
    name: "skin-tone",
    component: SkinTonePage,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
