import { defineStore } from "pinia";
import { ref } from "vue";

export const userLocationStore = defineStore("userLocation", {
  state: () => ({
    userLocation: ref({
      Suburb: "Not Set",
    }),
  }),
  getters: {
    // 返回一个 Map 结构，包含所有地址信息
    addressMap(state) {
      return state.userLocation;
    },

    hasLocation(state) {
      if (state.userLocation.Suburb === "Not Set") {
        return false;
      }
      return true;
    },
  },
  actions: {
    setUserLocation(location) {
      this.userLocation = location;
    },
  },
});
