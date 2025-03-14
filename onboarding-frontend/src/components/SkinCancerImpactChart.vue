<template>
  <div
    ref="uvImpactChart"
    id="uv-impact-chart"
    style="width: 100%; height: 400px"
  ></div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import * as echarts from "echarts";

const uvImpactChart = ref(null);

onMounted(() => {
  if (uvImpactChart.value) {
    const chart = echarts.init(uvImpactChart.value);

    const option = {
      title: {
        text: "Impact of Skin Cancer",
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
