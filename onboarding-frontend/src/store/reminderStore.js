import { defineStore } from "pinia";
import { ref } from "vue";

export const useReminderStore = defineStore("reminder", {
  state: () => ({
    reminders: ref([]),
  }),
  actions: {
    addReminder(departureTime, endTime) {
      this.reminders.push({ departureTime, endTime });
    },
  },
});
