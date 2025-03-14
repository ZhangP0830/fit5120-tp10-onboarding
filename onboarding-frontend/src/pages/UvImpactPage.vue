<template>
  <div id="uv-impact">
    <div class="skin-cancer-impact">
      <div class="chart-container">
        <SkinCancerIncidenceChart />
      </div>
      <div class="chart-container">
        <SkinCancerMortalityChart />
      </div>
    </div>

    <div class="heatForecast">
      <HeatForecastChart />
    </div>
  </div>
</template>

<script setup lang="js">

import HeatForecastChart from "@/components/HeatForecastChart.vue";
import SkinCancerIncidenceChart from "@/components/SkinCancerIncidenceChart.vue";
import SkinCancerMortalityChart from "@/components/SkinCancerMortalityChart.vue";
</script>

<style scoped>
#uv-impact {
  width: 80%;
}

.skin-cancer-impact {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  max-width: 1000px;
}

.chart-container {
  width: 100%;
  text-align: center;
  margin-bottom: 40px;
  padding: 20px;
  background: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

。heatForecast {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
