<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">Scan Site</RouterLink>
        <RouterLink to="/about">Learn</RouterLink>
        <RouterLink to="/about">About us</RouterLink>
      </nav>
    </div>
  </header>
  <div class="blank"></div>

  <RouterView />
</template>

<style scoped>
@import url("./assets/nav.css");
</style>
