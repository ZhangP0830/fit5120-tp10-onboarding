<template>
  <div class="container">
    <h1 class="title">Sunscreen Introduction</h1>
    <p class="description">
      Sunscreen use is one of five important ways of reducing the risk of skin
      cancer. The most comprehensive study of cancer prevention in Australia
      estimated that, in 2010, more than 1700 cases of melanoma and 14,190
      squamous cell carcinomas (a common keratinocyte cancer) were prevented by
      long-term sunscreen use.
    </p>

    <div class="section">
      <h2 class="subtitle">Select your skintone to get suggestion</h2>
      <a
        class="skinLink"
        href="https://www.cancer.nsw.gov.au/prevention-and-screening/preventing-cancer/preventing-skin-cancer/reduce-your-skin-cancer-risk/identify-your-skin-type"
        target="_blank"
      >
        Identify your skin tone to get personal recommendations.
      </a>
      <div class="select-container">
        <SkintoneSelect />
      </div>
    </div>

    <div class="section">
      <div class="recommendation-container">
        <SunProtectionCard />
      </div>
    </div>

    <div class="button-container">
      <ReminderButton />
    </div>
  </div>
</template>

<script setup lang="js">
import SkintoneSelect from "@/components/SkintoneSelect.vue";
import SunProtectionCard from "@/components/SunProtectionCard.vue";
import ReminderButton from "@/components/ReminderButton.vue";
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
}

.description {
  font-size: 16px;
  line-height: 1.5;
  margin-bottom: 20px;
  text-align: center;
  max-width: 600px;
}

.section {
  margin-bottom: 20px;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.subtitle {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 10px;
}

.skinLink {
  display: inline-block;
  margin-bottom: 10px;
  color: #007bff;
  text-decoration: none;
}

.skinLink:hover {
  text-decoration: underline;
}

.select-container {
  width: 100%;
  max-width: 400px;
}

.recommendation-container {
  display: flex;
  justify-content: center;
  width: 100%;
}

.button-container {
  margin-top: 20px;
  display: flex;
  justify-content: center;
  width: 100%;
}
</style>
