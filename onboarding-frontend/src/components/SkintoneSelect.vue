<template>
  <a-select
    v-model:value="selectedSkintone"
    :size="size"
    style="width: 400px"
    :options="options"
    @change="handleChange"
  ></a-select>
</template>

<script setup lang="js">
import { ref } from "vue";
import { userInformationStore } from "@/store/userInformationStore";

const userInformation = userInformationStore();

const selectedSkintone = ref(userInformation.userInformation.Skintone || null);
const size = "large";

const options = [
  { value: 1, label: "Always burns easily, extremely sun sensitive" },
  { value: 2, label: "Always burns easily, very sun sensitive" },
  { value: 3, label: "Sometimes burns, minimally sun sensitive" },
  { value: 4, label: "Burns minimally,  minimally sun sensitive" },
  { value: 5, label: "Rarely burns, skin not sensitive to sun" },
  { value: 6, label: "Never burns, deeply pigmented, skin not sensitive to sun" }
];

const handleChange = (value) => {
  userInformation.setSkintone(value);
};
</script>

<style scoped></style>
