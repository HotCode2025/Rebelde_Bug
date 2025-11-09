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
  { key: "habilidades", label: "Habilidades" },
  { key: "educacion", label: "Educación" },
  { key: "experiencia", label: "Experiencia" },
  { key: "proyectos", label: "Proyectos" },
  { key: "contacto", label: "Contacto" },
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
  display: flex; 
  align-items: center; 
  justify-content: space-between;
  padding: 16px 24px; 
  background: var(--color-bg-alt);
  border-bottom: 1px solid rgba(0,0,0,.08);
  position: sticky; 
  top: 0; 
  background: #fff; 
  z-index: 100;
}

.brand { 
  font-weight: 700;
  font-family: 'Orbitron', sans-serif;
  font-size: 1.2rem;
  color: var(--color-primary);
  text-shadow: 0 0 8px rgba(155, 92, 255, 0.5); 
}

ul { 
  display: flex; 
  gap: 1rem; 
  list-style: none; 
  margin: 0; 
  padding: 0; 
}

.link {
  background: transparent; 
  border: none; 
  padding: 8px 14px; 
  font-family: 'Poppins', sans-serif;
  cursor: pointer;
  letter-spacing: 0.5px;
  border-radius: 10px; 
  font-size: .95rem;
}

.link:hover {
  color: var(--color-secondary);
  text-shadow: 0 0 8px var(--color-secondary);
}


.link.active { 
  background: var(--color-primary); 
  color: var(--color-bg);
  box-shadow: 0 0 12px var(--color-primary); 
}

@media (max-width: 768px) {
  .nav {
    flex-direction: column;
    align-items: flex-start;
    padding: 12px 16px;
  }

  ul {
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-top: 8px;
  }

  .link {
    font-size: 0.9rem;
    padding: 6px 10px;
  }
}
</style>