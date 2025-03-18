<template>
  <div class="container">
    <SunscreenInfo />
    <ReminderSetup />
  </div>
  <ReminderInfo />
</template>

<script setup>
import SunscreenInfo from "@/components/SunscreenInfo.vue";
import ReminderSetup from "@/components/ReminderSetup.vue";
import ReminderInfo from "@/components/ReminderInfo.vue";
</script>

<style scoped>
.container {
  display: flex;
  justify-content: space-between;
  align-items: stretch;
  gap: 20px;
  max-width: 900px;
  margin: 20px auto;
}
</style>
