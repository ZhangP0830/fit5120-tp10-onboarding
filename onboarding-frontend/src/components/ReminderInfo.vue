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
  flex: 1;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
}
</style>
