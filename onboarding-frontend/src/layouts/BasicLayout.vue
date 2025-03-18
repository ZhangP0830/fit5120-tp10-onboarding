<!-- This file is the layout of whole website -->
<template>
  <div id="basic-layout">
    <a-layout>
      <!-- global Header of the website -->
      <a-layout-header class="header" :style="headerStyle">
        <GlobalHeader />
      </a-layout-header>
      <!-- Content of the website -->
      <a-layout-content class="content" :style="contentStyle">
        <div class="content-container">
          <router-view />
        </div>
      </a-layout-content>
    </a-layout>
  </div>
</template>

<script setup lang="js">
import GlobalHeader from "@/components/GlobalHeader.vue";
</script>

<style scoped>
#basic-layout .content {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  background: white;
}

.content-container {
  width: 90%;
}

#basic-layout .header {
  background: white;
  margin-bottom: 10px;
}
</style>
