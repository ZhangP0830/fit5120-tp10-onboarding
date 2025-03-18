<template>
  <div ref="heatForecastChart" id="heatForecastChart"></div>
</template>

<script setup>
import { onMounted, ref, watch } from "vue";
import * as echarts from "echarts";
import { userLocationStore } from "@/store/userLocationStore";
import { getWeatherForecast } from "@/api/data";

const heatForecastChart = ref(null);
const weatherData = ref([]);
const store = userLocationStore();

const fetchWeather = async () => {
  try {
    const lat = store.userLocation.lat;
    const lon = store.userLocation.lon;

    if (!lat || !lon) {
      console.error("Latitude or longitude is missing");
      return;
    }

    const response = await getWeatherForecast(lat, lon);
    weatherData.value = response;

    updateChart();
  } catch (error) {
    console.error("Failed to fetch weather data:", error);
  }
};

const updateChart = () => {
  if (heatForecastChart.value) {
    const chart = echarts.init(heatForecastChart.value);

    const option = {
      tooltip: { trigger: "axis" },
      xAxis: {
        type: "category",
        data: weatherData.value.map((d) => d.time),
        name: "Time",
      },
      yAxis: {
        type: "value",
        name: "Temperature (°C)",
      },
      series: [
        {
          data: weatherData.value.map((d) => d.temperature),
          type: "line",
          smooth: true,
        },
      ],
    };

    chart.setOption(option);
  }
};

watch(
  () => [store.userLocation.lat, store.userLocation.lon],
  () => {
    fetchWeather();
  }
);

onMounted(() => {
  fetchWeather();
});
</script>

<style scoped>
#heatForecastChart {
  width: 100%;
  height: 400px;
}
</style>
