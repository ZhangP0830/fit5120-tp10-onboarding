<template>
  <a-select
    v-model:value="value"
    show-search
    :default-active-first-option="false"
    :show-arrow="false"
    :not-found-content="null"
    placeholder="Select a suburb"
    style="width: 200px"
    :options="options"
    :filter-option="filterOption"
    @change="handleChange"
  ></a-select>
</template>

<script setup>
import { nextTick, onMounted, ref, watch } from "vue";
import { userLocationStore } from "@/store/userLocationStore";
import { fetchLocationData, getUvIndex } from "@/api/data";

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
  } else {
    console.warn("No location data found.");
  }
  await nextTick();

  const lat = userLocation.userLocation.lat;
  const lon = userLocation.userLocation.lon;
  console.log(lat, lon);
  if (lat && lon) {
    const uv_index = await getUvIndex(lat, lon);
    if (uv_index !== null) {
      userLocation.setIndex(uv_index);
    } else {
      userLocation.setIndex(null);
    }
  } else {
    console.warn("Latitude or longitude is missing, cannot fetch UV Index.");
  }
  console.log("Updated user location:", userLocation.userLocation);
};

const filterOption = (input, option) => {
  return option.value.toLowerCase().includes(input.toLowerCase());
};

onMounted(async () => {
  await loadOptions();

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
