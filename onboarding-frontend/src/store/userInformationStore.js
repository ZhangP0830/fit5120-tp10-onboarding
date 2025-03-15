import { defineStore } from "pinia";

export const userInformationStore = defineStore("userInformation", {
  state: () => ({
    userInformation: {
      Skintone: null,
    },
  }),
  actions: {
    setSkintone(skintone) {
      this.userInformation.Skintone = skintone;
    },
  },
});
