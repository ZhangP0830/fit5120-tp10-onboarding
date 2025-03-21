<template>
  <div>
    <div
      ref="skinCanerIncidenceChart"
      id="skinCanerIncidenceChart"
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
      this.chart.dispose();
      this.chart = null;
    }
  },
  methods: {
    async fetchData() {
      this.skinCancerData = await getSkinCancerIncidenceData();
      await this.$nextTick();
      this.drawChart();
    },
    drawChart() {
      if (!this.$refs.skinCanerIncidenceChart) {
        console.error("ECharts error：DOM null！");
        return;
      }

      if (!this.chart) {
        this.chart = echarts.init(this.$refs.skinCanerIncidenceChart);
      }

      const years = [...new Set(this.skinCancerData.map((item) => item.year))];
      const maleIncidence = this.skinCancerData
        .filter((d) => d.sex === "Males")
        .map((d) => d.incidence_rate);
      const femaleIncidence = this.skinCancerData
        .filter((d) => d.sex === "Females")
        .map((d) => d.incidence_rate);

      const option = {
        title: { text: "Melanoma Incidence", left: "center" },
        tooltip: {
          trigger: "axis",
          axisPointer: { type: "cross" },
          formatter: (params) => {
            let tooltipText = `<strong>Year: ${params[0].axisValue}</strong><br/>`;
            params.forEach((item) => {
              tooltipText += `${item.marker} <strong>${item.seriesName}:</strong> ${item.data} per 100k<br/>`;
            });
            return tooltipText;
          },
        },

        toolbox: {
          feature: {
            dataView: { show: true, readOnly: false },
            restore: { show: true },
            saveAsImage: { show: true },
          },
        },

        legend: { data: ["Male", "Female"], bottom: 0 },
        xAxis: { type: "category", data: years },
        yAxis: { type: "value", name: "Rate(Per 100k)" },
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
