<template>
  <div class="container">
    <img src="../assets/sunscreen2.jpg" class="left-image" />
    <div class="right-box">
      <SunscreenInfo />
      <ReminderSetup />
      <ReminderInfo />
    </div>
  </div>
</template>

<script setup>
import SunscreenInfo from "@/components/SunscreenInfo.vue";
import ReminderSetup from "@/components/ReminderSetup.vue";
import ReminderInfo from "@/components/ReminderInfo.vue";
</script>

<style scoped>
.container {
  display: flex;
  justify-content: flex-start;
  align-items: stretch;
  gap: 20px;
  width: 80%;
  margin: 20px auto;
}

.right-box {
  gap: 20px;
}

.left-image {
  width: 40%;
  height: auto;
  border-radius: 10px;
}
</style>
