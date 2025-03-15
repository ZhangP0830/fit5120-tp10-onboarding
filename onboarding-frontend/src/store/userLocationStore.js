import { defineStore } from "pinia";

export const userLocationStore = defineStore("userLocation", {
  state: () => ({
    userLocation: {
      Suburb: "Not Set",
      lat: null,
      lon: null,
    },
  }),
  getters: {
    addressMap(state) {
      return state.userLocation;
    },

    hasLocation(state) {
      return state.userLocation.Suburb !== "Not Set";
    },
  },
  actions: {
    setUserLocation({ Suburb, lat, lon }) {
      if (Suburb !== undefined) this.userLocation.Suburb = Suburb;
      if (lat !== undefined) this.userLocation.lat = lat;
      if (lon !== undefined) this.userLocation.lon = lon;
    },
  },
});
