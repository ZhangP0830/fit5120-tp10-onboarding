<template>
  <div class="container">
    <h2 class="title">Sun Protection Recommendations</h2>
    <!--  This is the current uv index  -->
    <div class="uv-index-display">
      Current UV Index: <strong>{{ uvIndex }}</strong>
    </div>
    <!--  These are the icon of different cloth  -->
    <div class="icon-container">
      <div class="icon-box">
        <img src="../assets/ico-cloth.svg" alt="Clothing" class="icon" />
        <p class="icon-label">Clothing</p>
      </div>
      <div class="icon-box">
        <img src="../assets/ico-hat.svg" alt="Hat" class="icon" />
        <p class="icon-label">Hat</p>
      </div>
      <div class="icon-box">
        <img src="../assets/ico-umbrella.svg" alt="Umbrella" class="icon" />
        <p class="icon-label">Umbrella</p>
      </div>
      <div class="icon-box">
        <img src="../assets/ico-glasses.svg" alt="Glasses" class="icon" />
        <p class="icon-label">Glasses</p>
      </div>
    </div>
    <!--  This div contains the table of cloth in different uv index  -->
    <div class="table-container">
      <a-table
        :columns="columns"
        :data-source="protectionData"
        bordered
        rowKey="uvIndex"
        class="table-style"
        pagination="false"
      />
    </div>
  </div>
</template>

<script setup>
import { computed } from "vue";
import { userLocationStore } from "@/store/userLocationStore";

const userLocation = userLocationStore();
const uvIndex = computed(() => userLocation.userLocation.uvIndex);
// Suggestion of clothing with different uv index.
const protectionData = [
  {
    uvIndex: "0 - 2",
    protection: "Wear regular clothing",
    clothing: "Optional hat and sunglasses",
  },
  {
    uvIndex: "3 - 5",
    protection: "Wear light long-sleeve clothing",
    clothing: "Hat and sunglasses",
  },
  {
    uvIndex: "6 - 7",
    protection: "Wear tightly woven long-sleeve clothing",
    clothing: "Wide-brimmed hat and UV-blocking sunglasses",
  },
  {
    uvIndex: "8 - 10",
    protection: "Wear sun-protective clothing",
    clothing: "Wide-brimmed hat and sunglasses",
  },
  {
    uvIndex: "11+",
    protection: "Wear full sun-protective clothing",
    clothing: "Wide-brimmed hat and certified UV-protection sunglasses",
  },
];

const columns = [
  { title: "UV Index", dataIndex: "uvIndex", key: "uvIndex" },
  { title: "Protection Level", dataIndex: "protection", key: "protection" },
  { title: "Recommended Clothing", dataIndex: "clothing", key: "clothing" },
];
</script>

<style scoped>
.container {
  padding: 20px;
  text-align: center;
  max-width: 900px;
  margin: auto;
}

.title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.uv-index-display {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 20px;
  color: #d9534f;
}

.icon-container {
  display: flex;
  justify-content: center;
  gap: 40px;
  margin-bottom: 20px;
}

.icon-box {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.icon {
  width: 70px;
  height: auto;
}

.icon-label {
  margin-top: 8px;
  font-size: 14px;
  font-weight: bold;
}

.table-container {
  display: flex;
  justify-content: center;
}

.table-style {
  width: 100%;
  max-width: 900px;
}
</style>
