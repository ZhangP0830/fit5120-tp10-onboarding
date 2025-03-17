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
} from "@ant-design/icons-vue";
import { useRouter } from "vue-router";
import SurburbSelect from "@/components/SurburbSelect.vue";

const router = useRouter();

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
    label: "Sunscreen",
    title: "Sunscreen",
  },
  {
    key: "/cloth-advice",
    icon: () => h(SkinFilled),
    label: "Cloth Advice",
    title: "Cloth Advice",
  },
]);
/*
 * Select user location
 * */
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
