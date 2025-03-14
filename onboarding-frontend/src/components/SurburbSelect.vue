<template>
  <a-select
    v-model:value="value"
    show-search
    placeholder="Select a person"
    style="width: 200px"
    :options="options"
    :filter-option="filterOption"
    @focus="handleFocus"
    @blur="handleBlur"
    @change="handleChange"
  ></a-select>
</template>

<script setup lang="js">
import { nextTick, onMounted, ref, watch } from "vue";
import { userLocationStore } from "@/store/userLocationStore";

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
    console.log(options.value);
  } catch (error) {
    console.error("Error loading options:", error);
  }
};

onMounted(() => {
  loadOptions();
});

const handleChange = value => {
  console.log(`selected ${value}`);
};
const handleBlur = () => {
  console.log("blur");
};
const handleFocus = () => {
  console.log("focus");
};
const filterOption = (input, option) => {
  return option.value.toLowerCase().indexOf(input.toLowerCase()) >= 0;
};

watch(value, async (newValue) => {
  if (newValue.length > 0) {
    await nextTick();
    userLocation.setUserLocation({
      Suburb: newValue[2] || "Not Set"
    });
  }
});
</script>

<style scoped></style>
