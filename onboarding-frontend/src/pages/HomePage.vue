<template>
  <div id="home-page">
    <h1 class="left-align">Are you well protected under the sun?</h1>
    <div class="image-container">
      <img src="../assets/beach.jpeg" alt="Beach Photo" class="beach-photo" />
    </div>

    <div class="uv-index-section">
      <h2 class="left-align">UV Index</h2>
      <p class="left-align">Please select a location to check the UV index:</p>
      <SurburbSelect class="suburb-select" />
      <UvVisual class="uv-visual" />
    </div>

    <div class="uv-legend">
      <div class="uv-box low">0-2<br />Low</div>
      <div class="uv-box moderate">3-5<br />Moderate</div>
      <div class="uv-box high">6-7<br />High</div>
      <div class="uv-box very-high">8-10<br />Very High</div>
      <div class="uv-box extreme">11+<br />Extreme</div>
    </div>

    <div class="heat-forecast-section">
      <h2 class="left-align">Forecast of Heat</h2>
      <p class="left-align">
        Forecasted temperature trend for the selected location over the next six
        hours.
      </p>
      <div v-if="hasValidSuburb">
        <HeatForecastChart class="heat-chart" />
      </div>
      <div v-else class="no-data">
        <a-empty description="No data available. Please select a suburb." />
      </div>
    </div>
  </div>
</template>

<script setup lang="js">
import UvVisual from "@/components/UvVisual.vue";
import HeatForecastChart from "@/components/HeatForecastChart.vue";
import SurburbSelect from "@/components/SurburbSelect.vue";
import { userLocationStore } from "@/store/userLocationStore";
import { computed } from "vue";

const userLocation = userLocationStore();
const hasValidSuburb = computed(() => userLocation?.userLocation?.Suburb !== "Not Set");
</script>

<style scoped>
#home-page {
  width: 90%;
  margin: auto;
}

.left-align {
  text-align: left;
}

.image-container {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.beach-photo {
  width: 100%;
  aspect-ratio: 3 / 1;
  border-radius: 10px;
}

.uv-index-section {
  margin-top: 20px;
}

.suburb-select {
  width: 250px;
  margin-top: 10px;
  margin-bottom: 10px;
}

.uv-legend {
  display: flex;
  justify-content: center;
  gap: 8px;
}

.uv-box {
  padding: 3px;
  border-radius: 5px;
  color: white;
  font-weight: bold;
  text-align: center;
  width: 70px;
}

.low {
  background: green;
}

.moderate {
  background: yellow;
  color: black;
  font-size: 14px;
}

.high {
  background: orange;
}

.very-high {
  background: red;
}

.extreme {
  background: violet;
}

.heat-forecast-section {
  margin-top: 30px;
}
</style>
