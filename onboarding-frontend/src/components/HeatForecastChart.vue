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
const store = userLocationStore(); // 获取全局 Store

// 获取天气数据
const fetchWeather = async () => {
  try {
    const lat = store.userLocation.lat;
    const lon = store.userLocation.lon;

    if (!lat || !lon) {
      console.error("Latitude or longitude is missing");
      return;
    }

    const response = await getWeatherForecast(lat, lon);
    console.log("*****************");
    console.log(response);
    console.log("*****************");
    weatherData.value = response;

    updateChart();
  } catch (error) {
    console.error("Failed to fetch weather data:", error);
  }
};

// 更新 ECharts
const updateChart = () => {
  if (heatForecastChart.value) {
    const chart = echarts.init(heatForecastChart.value);

    const option = {
      title: { text: "Forecast of Heat" },
      tooltip: { trigger: "axis" },
      xAxis: {
        type: "category",
        data: weatherData.value.map((d) => d.time),
      },
      yAxis: { type: "value" },
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

// 监听 `lat` 和 `lon` 变化，自动更新天气数据
watch(
  () => [store.userLocation.lat, store.userLocation.lon],
  () => {
    fetchWeather();
  }
);

// 组件挂载时获取数据
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
