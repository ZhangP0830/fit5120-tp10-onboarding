<template>
  <div class="card">
    <h3>Personalized Recommendations</h3>
    <p>{{ sunProtectionAdvice }}</p>
  </div>
</template>

<script setup>
import { userLocationStore } from "@/store/userLocationStore";
import { userInformationStore } from "@/store/userInformationStore";
import { computed } from "vue";

const userLocation = userLocationStore();
const userInformation = userInformationStore();

const sunProtectionAdvice = computed(() => {
  const uv_index = Number(userLocation.userLocation.uvIndex);
  const skintone = Number(userInformation.userInformation.Skintone);
  var number = 7;
  if (uv_index == null || skintone == null) {
    return "Please select your location and skintone.";
  }
  console.log("uv_index: ", uv_index, "  ", "skintone: ", skintone);
  if (skintone >= 3 && uv_index >= 0 && uv_index <= 3) {
    number = 0;
    console.log("number: ", number);
  }

  return `Based on your skin type and the UV index of your location, ${number} teaspoons of sunscreen should be applied 20 minutes before going outdoors.`;
});
</script>

<style scoped>
.card {
  width: 600px;
  padding: 20px;
  border-radius: 10px;
  background: white;
  box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
  text-align: center;
}

h3 {
  font-size: 18px;
  font-weight: bold;
}

p {
  font-size: 14px;
  color: #666;
  margin-bottom: 10px;
}
</style>
