<template>
  <div>
    <h3>UV Index Visualization</h3>
    <div ref="chart" style="width: 100%; height: 400px"></div>
  </div>
</template>

<script setup>
import { onMounted, ref, watch } from "vue";
import * as echarts from "echarts";
import { userLocationStore } from "@/store/userLocationStore";

const chart = ref(null);
const userLocation = userLocationStore();

const uvIndex = ref(userLocation.userLocation.uvIndex || 0);

const getUvLevel = (index) => {
  if (index <= 2) return "Low";
  if (index <= 5) return "Moderate";
  if (index <= 7) return "High";
  if (index <= 10) return "Very High";
  return "Extreme";
};

const uvColorMapping = [
  { min: 0, max: 2, color: "green" },
  { min: 3, max: 5, color: "yellow" },
  { min: 6, max: 7, color: "orange" },
  { min: 8, max: 10, color: "red" },
  { min: 11, max: 20, color: "violet" },
];

const renderChart = () => {
  if (!chart.value) return;
  const myChart = echarts.init(chart.value);

  const option = {
    title: {
      text: `Current UV Index: ${uvIndex.value} (${getUvLevel(uvIndex.value)})`,
      left: "center",
      textStyle: { fontSize: 16 },
    },
    visualMap: {
      show: false,
      min: 0,
      max: 20,
      inRange: {
        color: uvColorMapping.map((item) => item.color),
      },
    },
    series: [
      {
        type: "gauge",
        detail: { formatter: "{value}" },
        data: [{ value: uvIndex.value, name: "UV Index" }],
        min: 0,
        max: 20,
        axisLine: {
          lineStyle: {
            color: uvColorMapping.map((item) => [item.max / 20, item.color]),
          },
        },
      },
    ],
  };

  myChart.setOption(option);
};

watch(
  () => userLocation.userLocation.uvIndex,
  (newUvIndex) => {
    uvIndex.value = newUvIndex;
    renderChart();
  }
);

onMounted(() => {
  renderChart();
});
</script>

<style scoped>
h3 {
  text-align: center;
  margin-bottom: 10px;
}
</style>
