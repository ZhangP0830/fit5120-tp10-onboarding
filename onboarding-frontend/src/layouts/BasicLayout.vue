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
      <!-- Footer of the website -->
      <a-layout-footer class="footer" :style="footerStyle">
        Designed by FIT5120 TP10
      </a-layout-footer>
    </a-layout>
  </div>
</template>

<script setup lang="js">
import GlobalHeader from "@/components/GlobalHeader.vue";
</script>

<style scoped>
#basic-layout .footer {
  background: #efefef;
  text-align: center;
  padding: 16px;
  bottom: 0;
  right: 0;
  left: 0;
  position: fixed;
}

#basic-layout .content {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 40px 10%;
  background: white;
}

.content-container {
  width: 100%;
  max-width: 1000px;
}

#basic-layout .header {
  background: white;
  margin-bottom: 10px;
}
</style>
