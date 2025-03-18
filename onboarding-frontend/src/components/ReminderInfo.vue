<template>
  <div class="reminder-info">
    <h3>Reminder Info</h3>
    <template v-if="reminderStore.reminders.length > 0">
      <p>
        <strong>Departure Time:</strong> {{ formattedDepartureTime }}<br />
        <strong>End Time:</strong> {{ formattedEndTime }}<br />
        <strong>Notification Rule:</strong> First reminder 30 minutes before
        departure time, then every 2 hours until end time.
      </p>
    </template>
    <p v-else>No notification has been set.</p>
  </div>
</template>

<script setup>
import { computed } from "vue";
import { useReminderStore } from "@/store/reminderStore";
import dayjs from "dayjs";

const reminderStore = useReminderStore();

const latestReminder = computed(
  () => reminderStore.reminders[reminderStore.reminders.length - 1] || {}
);
const formattedDepartureTime = computed(() =>
  latestReminder.value.departureTime
    ? dayjs(latestReminder.value.departureTime).format("YYYY-MM-DD HH:mm")
    : ""
);
const formattedEndTime = computed(() =>
  latestReminder.value.endTime
    ? dayjs(latestReminder.value.endTime).format("YYYY-MM-DD HH:mm")
    : ""
);
</script>

<style scoped>
.reminder-info {
  margin-top: 20px;
  padding: 15px;
  border: 2px solid #007bff;
  border-radius: 8px;
  text-align: center;
  max-width: 500px;
  margin-left: auto;
  margin-right: auto;
  background-color: #eaf5ff;
}
</style>
