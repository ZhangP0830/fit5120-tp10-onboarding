<template>
  <h1>Sunscreen</h1>
  <p>
    Sunscreen use is one of five important ways of reducing the risk of skin
    cancer. The most comprehensive study of cancer prevention in Australia
    estimated that, in 2010, more than 1700 cases of melanoma and 14,190
    squamous cell carcinomas (a common keratinocyte cancer) were prevented by
    long-term sunscreen use.
  </p>
  <h2>Select your skintone to get suggestion</h2>
  <SkintoneSelect />
  <h2>Personal Recommendations</h2>
  <SunProtectionCard />
</template>

<script setup lang="js">
import SkintoneSelect from "@/components/SkintoneSelect.vue";
import SunProtectionCard from "@/components/SunProtectionCard.vue";
</script>

<style scoped></style>
