<template>
  <a-cascader
    id="location-select"
    v-model:value="value"
    :options="options"
    change-on-select
    placeholder="Please select"
  />
</template>
<script setup>
import { nextTick, ref, watch } from "vue";
import { userLocationStore } from "../store/userLocationStore";

const userLocation = userLocationStore();

const options = [
  {
    value: "zhejiang",
    label: "Zhejiang",
    children: [
      {
        value: "hangzhou",
        label: "Hangzhou",
        children: [
          {
            value: "xihu",
            label: "West Lake",
          },
        ],
      },
    ],
  },
  {
    value: "jiangsu",
    label: "Jiangsu",
    children: [
      {
        value: "nanjing",
        label: "Nanjing",
        children: [
          {
            value: "zhonghuamen",
            label: "Zhong Hua Men",
          },
        ],
      },
    ],
  },
];
const value = ref([]);

watch(value, async (newValue) => {
  if (newValue.length > 0) {
    await nextTick();
    userLocation.setUserLocation({
      State: newValue[0] || "Not Set",
      City: newValue[1] || "Not Set",
      Suburb: newValue[2] || "Not Set",
    });
  }
});
</script>
