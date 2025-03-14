<template>
  <div id="uv-impact">
    <div class="skinCancerImpact">
      <SkinCancerImpactChart />
    </div>
    <div class="heatForecast">
      <HeatForecastChart />
    </div>
  </div>
</template>

<script setup lang="js">

import SkinCancerImpactChart from "@/components/SkinCancerImpactChart.vue";
import HeatForecastChart from "@/components/HeatForecastChart.vue";
</script>

<style scoped>
#uv-impact {
  width: 80%;
}

.skinCancerImpact {
  display: flex;
  justify-content: center;
  align-items: center;
}

。heatForecast {
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
