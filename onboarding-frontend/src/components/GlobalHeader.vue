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
        />
      </a-col>
      <a-col flex="150px">
        <div class="location-select">
          <a-select
            v-model:value="userLocation"
            :size="size"
            style="width: 150px"
            :options="options"
          ></a-select>
        </div>
      </a-col>
    </a-row>
  </div>
</template>
<script setup>
import { h, ref } from "vue";
import {
  HomeFilled,
  AppstoreOutlined,
  SettingOutlined,
} from "@ant-design/icons-vue";

const current = ref(["mail"]);
const items = ref([
  {
    key: "mail",
    icon: () => h(HomeFilled),
    label: "Home",
    title: "Home",
  },
  {
    key: "app",
    icon: () => h(AppstoreOutlined),
    label: "Navigation Two",
    title: "Navigation Two",
  },
  {
    key: "sub1",
    icon: () => h(SettingOutlined),
    label: "Navigation Three - Submenu",
    title: "Navigation Three - Submenu",
    children: [
      {
        type: "group",
        label: "Item 1",
        children: [
          {
            label: "Option 1",
            key: "setting:1",
          },
          {
            label: "Option 2",
            key: "setting:2",
          },
        ],
      },
      {
        type: "group",
        label: "Item 2",
        children: [
          {
            label: "Option 3",
            key: "setting:3",
          },
          {
            label: "Option 4",
            key: "setting:4",
          },
        ],
      },
    ],
  },
  {
    key: "alipay",
    label: h(
      "a",
      {
        href: "https://antdv.com",
        target: "_blank",
      },
      "Navigation Four - Link"
    ),
    title: "Navigation Four - Link",
  },
]);
/*
 * Select user location
 * */
const userLocation = ref("");
</script>

<style scoped>
.title-bar {
  display: flex;
  align-items: center;
}

.logo {
  height: 64px;
}

.location-select {
  margin-right: 10px;
}
</style>
