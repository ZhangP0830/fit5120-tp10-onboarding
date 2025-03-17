<template>
  <div class="container">
    <a-card title="Sunscreen Reminder" class="card">
      <!-- 选择位置 -->
      <a-form-item label="Select Location">
        <a-input v-model="selectedLocation" placeholder="Enter your location" />
      </a-form-item>

      <!-- 选择外出时间 -->
      <a-form-item label="Select Time">
        <a-time-picker v-model="selectedTime" format="HH:mm" />
      </a-form-item>
      <a-button
        type="primary"
        @click="toggleReminder"
        :disabled="!selectedTime"
      >
        {{ reminderOn ? "Turn Off Reminder" : "Turn On Reminder" }}
      </a-button>

      <!-- 提醒状态 -->
      <div v-if="reminderOn" class="reminder-info">
        Reminder is ON. You will be notified 2 hours before and every 2 hours.
      </div>
    </a-card>
  </div>
</template>

<script>
import { message } from "ant-design-vue";

export default {
  data() {
    return {
      selectedLocation: "",
      selectedTime: null,
      reminderOn: false,
      reminderIntervals: [],
    };
  },
  methods: {
    toggleReminder() {
      if (this.reminderOn) {
        this.clearReminders();
        this.reminderOn = false;
        message.info("Reminder turned off.");
      } else {
        this.setReminders();
        this.reminderOn = true;
        message.success("Reminder turned on.");
      }
    },
    setReminders() {
      if (!this.selectedTime) {
        message.error("Please select a time first.");
        return;
      }

      this.clearReminders();
      const selectedHour = this.selectedTime.hour();
      const selectedMinute = this.selectedTime.minute();
      const now = new Date();
      const selectedDate = new Date(now);
      selectedDate.setHours(selectedHour, selectedMinute, 0, 0);

      const twoHoursBefore = new Date(selectedDate);
      twoHoursBefore.setHours(selectedHour - 2);
      this.scheduleNotification(twoHoursBefore, "Apply sunscreen in 2 hours!");

      for (let i = 0; i < 6; i++) {
        const reminderTime = new Date(selectedDate);
        reminderTime.setHours(selectedHour + i * 2);
        this.scheduleNotification(reminderTime, "Apply sunscreen!");
      }
    },
    scheduleNotification(time, messageText) {
      const now = new Date();
      const delay = time - now;
      if (delay > 0) {
        const timeout = setTimeout(() => {
          message.info(messageText);
        }, delay);
        this.reminderIntervals.push(timeout);
      }
    },
    clearReminders() {
      this.reminderIntervals.forEach(clearTimeout);
      this.reminderIntervals = [];
    },
  },
};
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f5f5;
}

.card {
  width: 400px;
}

.reminder-info {
  margin-top: 10px;
  padding: 10px;
  background: #e6f7ff;
  border: 1px solid #91d5ff;
  border-radius: 5px;
}
</style>
