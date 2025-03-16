<template>
  <div>
    <a-button type="primary" @click="goToReminderPage"> Set Reminder</a-button>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

const goToReminderPage = () => {
  router.push("/sunscreen/reminder");
};
</script>
