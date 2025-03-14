<template>
  <div>
    <div
      ref="uvImpactChart"
      id="uvimpact-chart"
      style="width: 100%; height: 400px"
    ></div>
  </div>
</template>

<script>
import { getSkinCancerIncidenceData } from "@/api/data.js";
import * as echarts from "echarts";

export default {
  data() {
    return {
      chart: null,
      skinCancerData: [],
    };
  },
  async mounted() {
    await this.fetchData();
  },
  beforeUnmount() {
    if (this.chart) {
      this.chart.dispose(); // 释放 ECharts 资源
      this.chart = null;
    }
  },
  methods: {
    async fetchData() {
      this.skinCancerData = await getSkinCancerIncidenceData();
      console.log(this.skinCancerData);
      await this.$nextTick(); // 确保 DOM 已渲染
      this.drawChart();
    },
    drawChart() {
      if (!this.$refs.uvImpactChart) {
        console.error("ECharts error：DOM null！");
        return;
      }

      if (!this.chart) {
        this.chart = echarts.init(this.$refs.uvImpactChart);
      }

      const years = [...new Set(this.skinCancerData.map((item) => item.year))];
      const maleIncidence = this.skinCancerData
        .filter((d) => d.sex === "Males")
        .map((d) => d.incidence_rate);
      const femaleIncidence = this.skinCancerData
        .filter((d) => d.sex === "Females")
        .map((d) => d.incidence_rate);

      const option = {
        title: { text: "Skin Cancer Incidence", left: "center" },
        tooltip: { trigger: "axis" },
        legend: { data: ["Male", "Female"], bottom: 0 },
        xAxis: { type: "category", data: years },
        yAxis: { type: "value", name: "Incidence Rate(Per 100,000)" },
        series: [
          {
            name: "Male",
            type: "line",
            data: maleIncidence,
            color: "red",
          },
          {
            name: "Female",
            type: "line",
            data: femaleIncidence,
            color: "blue",
          },
        ],
      };

      this.chart.setOption(option);
    },
  },
};
</script>
