<template>
  <div class="reminder-container">
    <a-date-picker
      v-model:value="startTime"
      show-time
      :disabled-date="disablePastDates"
      placeholder="Select Start Time"
    />
    <a-date-picker
      v-model:value="endTime"
      show-time
      :disabled-date="disablePastDates"
      placeholder="Select End Time"
    />
    <a-button type="primary" @click="setReminder">Set Reminder</a-button>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { notification } from "ant-design-vue";
import dayjs from "dayjs";

const startTime = ref(null);
const endTime = ref(null);

const disablePastDates = (current) => {
  return current && current.isBefore(dayjs());
};

const setReminder = () => {
  if (!startTime.value || !endTime.value) {
    notification.error({
      message: "Error",
      description: "Please select both start and end time.",
    });
    return;
  }

  const now = dayjs();
  const start = dayjs(startTime.value);
  const end = dayjs(endTime.value);

  if (start.isBefore(now)) {
    notification.error({
      message: "Invalid Time",
      description: "Start time cannot be in the past.",
    });
    return;
  }

  if (end.isBefore(start)) {
    notification.error({
      message: "Invalid Time",
      description: "End time cannot be before start time.",
    });
    return;
  }

  scheduleNotifications(start, end);

  notification.success({
    message: "Reminder Set",
    description: `Reminders will start at ${start.format(
      "HH:mm"
    )} and end at ${end.format("HH:mm")}.`,
  });
};

const scheduleNotifications = (start, end) => {
  const now = dayjs();
  let firstReminderTime = start.subtract(30, "minute"); // 默认提前 30 分钟提醒

  if (firstReminderTime.isBefore(now)) {
    firstReminderTime = start;
  }

  let reminderTime = firstReminderTime;

  while (reminderTime.isBefore(end)) {
    setTimeout(() => {
      notification.info({
        message: "Sunscreen Reminder",
        description: `Time to use sunscreen!`,
        duration: 5,
      });
    }, reminderTime.diff(now, "millisecond"));

    reminderTime = reminderTime.add(2, "hour");
  }
  console.log(
    `Scheduling notification in ${reminderTime.diff(now, "millisecond")} ms`
  );
};
</script>

<style scoped>
.reminder-container {
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 300px;
  margin: auto;
}
</style>
