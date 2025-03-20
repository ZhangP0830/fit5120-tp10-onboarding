<template>
  <div class="reminder-box">
    <h2 class="subtitle">Set Your Sunscreen Reminder</h2>
    <div class="input-row">
      <label for="departure-time">Departure Time:</label>
      <a-date-picker
        id="departure-time"
        v-model:value="departureTime"
        show-time
        :disabled-date="disablePastDates"
        placeholder="Select"
        class="date-picker"
      />
    </div>
    <div class="input-row">
      <label for="end-time">End Time:</label>
      <a-date-picker
        id="end-time"
        v-model:value="endTime"
        show-time
        :disabled-date="disablePastDates"
        placeholder="Select"
        class="date-picker"
      />
    </div>
    <a-button type="primary" @click="setReminder" class="reminder-button"
      >Set Reminder
    </a-button>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useReminderStore } from "@/store/reminderStore";
import { notification } from "ant-design-vue";
import dayjs from "dayjs";

const departureTime = ref(null);
const endTime = ref(null);
const reminderStore = useReminderStore();

const disablePastDates = (current) => {
  return current && current.isBefore(dayjs(), "day");
};

const setReminder = () => {
  if (!departureTime.value || !endTime.value) {
    notification.error({
      message: "Error",
      description: "Please select both departure and end time.",
    });
    return;
  }

  if (dayjs(departureTime.value).isBefore(dayjs())) {
    notification.error({
      message: "Invalid Time",
      description: "Departure time cannot be in the past.",
    });
    return;
  }

  if (dayjs(endTime.value).isBefore(dayjs(departureTime.value))) {
    notification.error({
      message: "Invalid Time",
      description: "End time cannot be before departure time.",
    });
    return;
  }

  reminderStore.addReminder(departureTime.value, endTime.value);

  notification.success({
    message: "Reminder Set",
    description: `Reminders will start at ${dayjs(departureTime.value).format(
      "HH:mm"
    )} 
                  and end at ${dayjs(endTime.value).format("HH:mm")}.`,
  });
};
</script>

<style scoped>
.reminder-box {
  flex: 1;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
}

.input-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  width: 100%;
}

.date-picker {
  width: 150px;
}

.reminder-button {
  width: 30%;
  align-self: center;
}
</style>
