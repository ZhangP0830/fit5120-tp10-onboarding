<template>
  <div>
    <div
      ref="skinCanerMortalityChart"
      id="skinCanerMortalityChart"
      style="width: 100%; height: 400px"
    ></div>
  </div>
</template>

<script>
import { getSkinCancerMortalityData } from "@/api/data.js";
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
      this.skinCancerData = await getSkinCancerMortalityData();
      console.log(this.skinCancerData);
      await this.$nextTick();
      this.drawChart();
    },
    drawChart() {
      if (!this.$refs.skinCanerMortalityChart) {
        console.error("ECharts error：DOM null！");
        return;
      }

      if (!this.chart) {
        this.chart = echarts.init(this.$refs.skinCanerMortalityChart);
      }

      const years = [...new Set(this.skinCancerData.map((item) => item.year))];
      const maleMortality = this.skinCancerData
        .filter((d) => d.sex === "Males")
        .map((d) => d.mortality_rate);
      const femaleMortality = this.skinCancerData
        .filter((d) => d.sex === "Females")
        .map((d) => d.mortality_rate);

      const option = {
        title: { text: "Skin Cancer Mortality", left: "center" },
        tooltip: { trigger: "axis" },
        legend: { data: ["Male", "Female"], bottom: 0 },
        xAxis: { type: "category", data: years },
        yAxis: { type: "value", name: "Mortality Rate(Per 100k)" },
        series: [
          {
            name: "Male",
            type: "line",
            data: maleMortality,
            color: "red",
          },
          {
            name: "Female",
            type: "line",
            data: femaleMortality,
            color: "blue",
          },
        ],
      };

      this.chart.setOption(option);
    },
  },
};
</script>
