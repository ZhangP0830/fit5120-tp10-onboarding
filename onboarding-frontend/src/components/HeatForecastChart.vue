<template>
  <div
    ref="heatForecastChart"
    id="heatForecastChart"
    style="width: 100%; height: 400px"
  ></div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import * as echarts from "echarts";

const heatForecastChart = ref(null);

onMounted(() => {
  if (heatForecastChart.value) {
    const chart = echarts.init(heatForecastChart.value);

    const option = {
      title: {
        text: "Forecast of Heat",
      },
      tooltip: {
        trigger: "axis",
      },
      xAxis: {
        type: "category",
        data: ["1pm", "3pm", "5pm", "7pm"],
      },
      yAxis: {
        type: "value",
      },
      series: [
        {
          data: [13, 20, 15, 10], // 直接写死数据
          type: "line",
          smooth: true,
        },
      ],
    };

    chart.setOption(option);
  }
});
</script>

<style scoped>
#uv-impact-chart {
  width: 100%;
  height: 400px;
}
</style>
