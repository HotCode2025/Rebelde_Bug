<script setup>
// Menú del portafolio grupal
import { defineEmits, defineProps } from "vue";
const emit = defineEmits(["change"]);
const props = defineProps({
  active: { type: String, default: "inicio" }
});

const items = [
  { key: "inicio", label: "Inicio" },
  { key: "integrantes", label: "Integrantes" },
  { key: "educacion", label: "Educación" },
  { key: "experiencia", label: "Experiencia" },
  { key: "proyectos", label: "Proyectos" },
];

function go(key) { emit("change", key); }
</script>

<template>
  <nav class="nav">
    <div class="brand">Portafolio Grupal</div>
    <ul>
      <li v-for="it in items" :key="it.key">
        <button
          class="link"
          :class="{ active: props.active === it.key }"
          @click="go(it.key)"
        >
          {{ it.label }}
        </button>
      </li>
    </ul>
  </nav>
</template>

<style scoped>
.nav {
  display: flex; align-items: center; justify-content: space-between;
  padding: 12px 16px; border-bottom: 1px solid rgba(0,0,0,.08);
  position: sticky; top: 0; background: #fff; z-index: 50;
}
.brand { font-weight: 700; }
ul { display: flex; gap: 8px; list-style: none; margin: 0; padding: 0; }
.link {
  background: transparent; border: none; padding: 8px 12px; cursor: pointer;
  border-radius: 10px; font-size: .95rem;
}
.link.active { background: #111827; color: #fff; }
</style>