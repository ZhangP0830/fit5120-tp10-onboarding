<template>
  <div
    ref="stateUvIndexChart"
    id="stateUvIndexChart"
    style="width: 100%; height: 400px"
  ></div>
</template>

<script setup lang="js">
import { ref, onMounted } from "vue";
import * as echarts from "echarts";

const stateUvIndexChart = ref(null);

onMounted(() => {
  const chart = echarts.init(stateUvIndexChart.value);

  const option = {
    tooltip: {
      trigger: "axis",
      axisPointer: {
        type: "shadow"
      }
    },
    grid: {
      left: "3%",
      right: "4%",
      bottom: "3%",
      containLabel: true
    },
    xAxis: [
      {
        type: "category",
        data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        axisTick: {
          alignWithLabel: true
        }
      }
    ],
    yAxis: [
      {
        type: "value"
      }
    ],
    series: [
      {
        name: "Direct",
        type: "bar",
        barWidth: "60%",
        data: [10, 52, 200, 334, 390, 330, 220]
      }
    ]
  };

  chart.setOption(option);
});
</script>

<style scoped></style>
