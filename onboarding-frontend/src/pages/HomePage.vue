<template>
  <div id="home-page">
    <div class="uv-level">
      <h1>UV Level</h1>
      <p>Please select your location to see the UV index:</p>
      <UvVisual />
    </div>
    <div class="heatForecast">
      <h1>Forecast of Heat</h1>
      <p>Please select your location to see the heat forecast:</p>
      <HeatForecastChart />
    </div>
  </div>
</template>

<script setup lang="js">
import UvVisual from "@/components/UvVisual.vue";
import HeatForecastChart from "@/components/HeatForecastChart.vue";
</script>

<style scoped></style>
