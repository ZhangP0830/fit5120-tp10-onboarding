import { defineStore } from "pinia";
import { ref } from "vue";

export const useReminderStore = defineStore("reminder", {
  state: () => ({
    reminders: ref([]),
  }),
  actions: {
    addReminder(startTime, endTime) {
      this.reminders.push({ startTime, endTime });
    },
  },
});
