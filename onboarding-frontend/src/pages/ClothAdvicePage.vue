<template>
  <div class="container">
    <h2>Sun Protection Recommendations</h2>

    <a-table
      :columns="columns"
      :data-source="protectionData"
      bordered
      rowKey="uvIndex"
      class="table-style"
    />
  </div>
</template>

<script setup>
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
}

.table-style {
  margin-top: 20px;
}
</style>
