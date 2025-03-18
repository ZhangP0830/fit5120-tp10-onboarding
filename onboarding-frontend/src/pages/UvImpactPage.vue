<template>
  <div id="uv-impact">
    <div class="skin-cancer-impact">
      <div class="chart-section">
        <div class="chart-container">
          <SkinCancerIncidenceChart />
        </div>
        <div class="description-container">
          <div class="content">
            <h2>Melanoma Incidence Trends</h2>
            <h3>Overview</h3>
            <p>
              Melanoma incidence rates have steadily increased over time, with
              males consistently having higher rates than females, though both
              genders show upward trends.
            </p>

            <h3>Key Trends:</h3>
            <ul>
              <li>
                <strong>1982:</strong> Around 20 cases per 100,000 for both
                males and females.
              </li>
              <li><strong>2024:</strong></li>
              <ul>
                <li>Males: Over 80 cases per 100,000 people.</li>
                <li>Females: Approximately 60 cases per 100,000 people.</li>
              </ul>
            </ul>

            <h3>Possible Causes:</h3>
            <ul>
              <li>
                <strong>Increased UV Exposure:</strong> More exposure from
                outdoor activities.
              </li>
              <li>
                <strong>Lifestyle Changes:</strong> Such as tanning habits.
              </li>
              <li>
                <strong>Advancements in Detection:</strong> Leading to more
                diagnosed cases.
              </li>
            </ul>
          </div>
        </div>
      </div>

      <div class="chart-section">
        <div class="chart-container">
          <SkinCancerMortalityChart />
        </div>
        <div class="description-container">
          <div class="content">
            <h2>Melanoma Mortality Trends</h2>
            <h3>Overview</h3>
            <p>
              Melanoma mortality rates have followed different patterns for
              males and females, with males peaking before declining and females
              maintaining a relatively stable rate over time.
            </p>

            <h3>Key Trends</h3>
            <ul>
              <li>
                <strong>Males:</strong> Increased from 5 per 100,000 (1982),
                peaked at 10 per 100,000 (early 2010s), then declined.
              </li>
              <li>
                <strong>Females:</strong> Fluctuated between 3 to 5 per 100,000,
                with a slight decline in recent years.
              </li>
            </ul>

            <h3>Possible Causes</h3>
            <ul>
              <li>
                <strong>Improved Treatments:</strong> Enhancing survival rates.
              </li>
              <li>
                <strong>Early Detection:</strong> Leading to better outcomes.
              </li>
              <li>
                <strong>Awareness Campaigns:</strong> Encouraging timely medical
                attention.
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import SkinCancerIncidenceChart from "@/components/SkinCancerIncidenceChart.vue";
import SkinCancerMortalityChart from "@/components/SkinCancerMortalityChart.vue";
</script>

<style scoped>
#uv-impact {
  width: 80%;
  margin: 0 auto;
}

.skin-cancer-impact {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  max-width: 1000px;
}

.chart-section {
  display: flex;
  justify-content: space-between;
  align-items: stretch;
  width: 100%;
  margin-bottom: 40px;
  gap: 20px;
}

.chart-container,
.description-container {
  flex: 1;
  padding: 20px;
  background: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  min-height: 100%;
}

.description-container {
  text-align: left;
  background: #ffffff;
}

.description-container h2 {
  font-size: 22px;
  margin-bottom: 10px;
}

.description-container h3 {
  font-size: 18px;
  margin-top: 15px;
  margin-bottom: 10px;
}

.description-container ul {
  padding-left: 20px;
}

.description-container li {
  margin-bottom: 8px;
  line-height: 1.6;
}
</style>
