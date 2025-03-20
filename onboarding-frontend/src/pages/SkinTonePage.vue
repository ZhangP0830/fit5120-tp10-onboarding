<template>
  <div class="container">
    <h2 class="title">Sun Protection Recommendations</h2>
    <div class="uv-index-display">
      Current UV Index: <strong>{{ uvIndex }}</strong>
    </div>
    <a-card class="card">
      <a-alert :message="uvAdvice" type="info" show-icon />
    </a-card>

    <div class="image-grid">
      <div v-for="(tone, index) in skinTones" :key="index" class="image-box">
        <img :src="tone.image" :alt="tone.label" class="tone-image" />
        <p class="tone-type">Teaspoons: {{ getTeaspoons(index + 1) }}</p>
        <p class="tone-label">{{ tone.label }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { computed, defineComponent } from "vue";
import { userLocationStore } from "@/store/userLocationStore";

export default defineComponent({
  setup() {
    const userLocation = userLocationStore();
    const uvIndex = computed(() => userLocation.userLocation.uvIndex);
    // Set the information of the different uv index.
    const uvAdvice = computed(() => {
      if (uvIndex.value < 3) return "Low UV: No special protection needed.";
      if (uvIndex.value < 6) return "Moderate UV: Use SPF 30+ sunscreen.";
      if (uvIndex.value < 8) return "High UV: Use SPF 50+ sunscreen";
      if (uvIndex.value < 11)
        return "Very High UV: Avoid direct sun exposure, use strong protection.";
      return "Extreme UV: Stay indoors or seek shade.";
    });
    // Set uv range and teaspoons amount.
    const teaspoonsData = [
      { uvRange: [0, 2.99], teaspoons: [7, 7, 0, 0, 0, 0] },
      { uvRange: [3, 4.99], teaspoons: [7, 7, 7, 7, 7, 7] },
      { uvRange: [5, 6.99], teaspoons: [7, 7, 7, 7, 7, 7] },
      { uvRange: [7, 11], teaspoons: [7, 7, 7, 7, 7, 7] },
      { uvRange: [11, Infinity], teaspoons: [7, 7, 7, 7, 7, 7] },
    ];

    const getTeaspoons = (skinType) => {
      const range = teaspoonsData.find(
        (range) =>
          uvIndex.value >= range.uvRange[0] && uvIndex.value <= range.uvRange[1]
      );
      return range ? range.teaspoons[skinType - 1] : "N/A";
    };
    // Display the different skin tone with image and text.
    const skinTones = [
      {
        image: new URL("../assets/skin-type-1.png", import.meta.url).href,
        label: "Always burns easily, sun sensitive",
      },
      {
        image: new URL("../assets/skin-type-2.png", import.meta.url).href,
        label: "Burns easily, tans minimally",
      },
      {
        image: new URL("../assets/skin-type-3.png", import.meta.url).href,
        label: "Burns moderately, tans gradually",
      },
      {
        image: new URL("../assets/skin-type-4.png", import.meta.url).href,
        label: "Burns minimally, tans easily",
      },
      {
        image: new URL("../assets/skin-type-5.png", import.meta.url).href,
        label: "Rarely burns, tans profusely",
      },
      {
        image: new URL("../assets/skin-type-6.png", import.meta.url).href,
        label: "Never burns, deeply pigmented",
      },
    ];

    return { uvIndex, uvAdvice, skinTones, getTeaspoons };
  },
});
</script>

<style scoped>
.container {
  width: 90%;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.card {
  margin-bottom: 20px;
}

.image-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px 30px;
  justify-items: center;
  align-items: center;
}

.tone-image {
  width: 120px;
  height: 120px;
  object-fit: contain;
  border-radius: 10px;
}

.tone-type {
  font-weight: bold;
  font-size: 16px;
  margin-top: 10px;
}

.tone-label {
  font-size: 14px;
  color: #555;
  max-width: 140px;
  margin: auto;
  text-align: center;
  line-height: 1.5;
}

.uv-index-display {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 20px;
  color: #d9534f;
}
</style>
