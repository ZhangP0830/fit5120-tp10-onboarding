<template>
  <a-select
    v-model:value="value"
    show-search
    placeholder="Select a suburb"
    style="width: 200px"
    :options="options"
    :filter-option="filterOption"
    @focus="handleFocus"
    @blur="handleBlur"
    @change="handleChange"
  ></a-select>
</template>

<script setup>
import { nextTick, onMounted, ref, watch } from "vue";
import { userLocationStore } from "@/store/userLocationStore";
import { fetchLocationData } from "@/api/data";

const options = ref([]);
const value = ref(null);
const userLocation = userLocationStore();

const loadOptions = async () => {
  try {
    const response = await fetch("/states.txt");
    const text = await response.text();
    options.value = text
      .split("\n")
      .map((item) => item.trim())
      .filter((item) => item)
      .map((item) => ({ label: item, value: item }));
    console.log("Loaded options:", options.value);
  } catch (error) {
    console.error("Error loading options:", error);
  }
};

const handleChange = async (suburb) => {
  console.log(`Selected: ${suburb}`);
  value.value = suburb;
  userLocation.setUserLocation({ Suburb: suburb });
  const locationData = await fetchLocationData(suburb);
  if (locationData) {
    await nextTick();
    userLocation.setUserLocation(locationData);
    console.log("Updated user location:", userLocation.userLocation);
    console.log(userLocation.userLocation);
  } else {
    console.warn("No location data found.");
  }
};

const handleBlur = () => {
  console.log("blur");
};

const handleFocus = () => {
  console.log("focus");
};

/**
 * 过滤搜索框输入
 */
const filterOption = (input, option) => {
  return option.value.toLowerCase().includes(input.toLowerCase());
};

// 页面加载时初始化 suburb 选项，并默认选择全局变量的 suburb
onMounted(async () => {
  await loadOptions(); // ✅ 确保 options 加载完毕
  console.log("Options loaded:", options.value);

  if (userLocation.userLocation.Suburb !== "Not Set") {
    value.value = userLocation.userLocation.Suburb;
    console.log("Default selected value:", value.value);
  }
});

watch(
  () => userLocation.userLocation.Suburb,
  (newSuburb) => {
    if (newSuburb !== "Not Set") {
      value.value = newSuburb;
    }
  },
  { deep: true }
);
</script>

<style scoped></style>
