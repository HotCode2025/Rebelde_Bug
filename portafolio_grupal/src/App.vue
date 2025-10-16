<!-- src/App.vue -->
<script setup>
import { ref } from "vue";
import NavBar from "@/components/NavBar.vue";
import Inicio from "@/components/Inicio.vue";
import DatosIntegrantes from "@/components/DatosIntegrantes.vue";
import Educacion from "@/components/Educacion.vue";
import Experiencia from "@/components/Experiencia.vue";

const section = ref("inicio");
function onChange(key) { section.value = key; }
</script>

<template>
  <NavBar :active="section" @change="onChange" />

  <main>
    <Inicio v-if="section === 'inicio'" @change="onChange" />
    <DatosIntegrantes v-else-if="section === 'integrantes'" />
    <Educacion v-else-if="section === 'educacion'" />
    <Experiencia v-else-if="section === 'experiencia'" />
  </main>
</template>

<style scoped>
main{ background: #f7f9fb; min-height: calc(100vh - 56px); }
</style>
