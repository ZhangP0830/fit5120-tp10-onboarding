<template>
  <div id="global-header">
    <a-row :wrap="false">
      <a-col flex="100px">
        <div class="title-bar">
          <img class="logo" src="../assets/image.jpeg" alt="logo" />
        </div>
      </a-col>
      <a-col flex="auto">
        <a-menu
          v-model:selectedKeys="current"
          mode="horizontal"
          :items="items"
          @click="clickMenu"
        />
      </a-col>
      <a-col flex="200px">
        <div class="location-select">
          <SurburbSelect />
        </div>
      </a-col>
    </a-row>
  </div>
</template>
<script setup>
import { h, ref } from "vue";
import {
  ExperimentFilled,
  HomeFilled,
  SignalFilled,
  SkinFilled,
  SmileFilled,
} from "@ant-design/icons-vue";
import { useRouter } from "vue-router";
import SurburbSelect from "@/components/SurburbSelect.vue";

const router = useRouter();
// Change the click path
const clickMenu = (menuItem) => {
  const key = menuItem.key;
  router.push({
    path: key,
  });
};

const current = ref(["/"]);
router.afterEach((to) => {
  current.value = [to.path];
});

// The details of the tab
const items = ref([
  {
    key: "/",
    icon: () => h(HomeFilled),
    label: "Home",
    title: "Home",
  },
  {
    key: "/uv-impact",
    icon: () => h(SignalFilled),
    label: "UV Impact",
    title: "UV Impact",
  },
  {
    key: "/sunscreen",
    icon: () => h(ExperimentFilled),
    label: "Sunscreen Reminder",
    title: "Sunscreen Reminder",
  },
  {
    key: "/cloth-advice",
    icon: () => h(SkinFilled),
    label: "Clothing Advice",
    title: "Clothing Advice",
  },
  {
    key: "/skin-tone",
    icon: () => h(SmileFilled),
    label: "Skin Tone",
    title: "Skin Tone",
  },
]);
</script>

<style scoped>
.title-bar {
  display: flex;
  align-items: center;
}

.logo {
  height: 64px;
}
</style>
