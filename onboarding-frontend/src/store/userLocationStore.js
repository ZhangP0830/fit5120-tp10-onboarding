import { defineStore } from "pinia";

export const userLocationStore = defineStore("userLocation", {
  state: () => ({
    userLocation: {
      Suburb: "Not Set",
      lat: null,
      lon: null,
      uvIndex: 0,
    },
  }),
  getters: {
    addressMap(state) {
      return state.userLocation;
    },

    hasLocation(state) {
      return state.userLocation.Suburb !== "Not Set";
    },

    getUVIndex(state) {
      return state.userLocation.uvIndex;
    },
  },
  actions: {
    setUserLocation({ Suburb, lat, lon }) {
      if (Suburb !== undefined) this.userLocation.Suburb = Suburb;
      if (lat !== undefined) this.userLocation.lat = lat;
      if (lon !== undefined) this.userLocation.lon = lon;
    },

    setIndex(index) {
      if (index !== undefined) this.userLocation.uvIndex = index;
    },
  },
});
