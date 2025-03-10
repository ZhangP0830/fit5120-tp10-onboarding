<template>
  <div id="basic-layout">
    <a-layout>
      <a-layout-header class="footer" :style="headerStyle"
        >Header
      </a-layout-header>
      <a-layout-content class="content" :style="contentStyle">
        <router-view />
      </a-layout-content>
      <a-layout-footer class="footer" :style="footerStyle"
        >Footer
      </a-layout-footer>
    </a-layout>
  </div>
</template>

<script setup lang="js"></script>

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
  padding: 20px;
  margin-bottom: 20px;
  baclkground: linear-gradient(to right, white, gray);
}
</style>
