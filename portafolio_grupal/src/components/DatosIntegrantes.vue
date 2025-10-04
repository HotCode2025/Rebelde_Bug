<!-- src/components/DatosIntegrantes.vue -->
<script setup>
import { computed } from "vue";
import { integrantes as RAW } from "@/data/integrantes.js";

/** Orden opcional por nombre (o por id si preferís) */
const integrantes = computed(() =>
  [...RAW].sort((a, b) => a.nombre.localeCompare(b.nombre))
);

function initials(name) {
  return name
    .split(" ")
    .filter(Boolean)
    .slice(0, 2)
    .map(w => w[0]?.toUpperCase())
    .join("");
}
</script>

<template>
  <section id="integrantes" class="grupo">
    <header class="encabezado">
      <h2>Integrantes del equipo</h2>
      <p>Los datos se leen directamente del código en <code>src/data/integrantes.js</code>.</p>
    </header>

    <div class="grid">
      <article
        v-for="m in integrantes"
        :key="m.id"
        class="card"
      >
        <div class="card-header">
          <div class="avatar" :title="m.nombre">
            <img v-if="m.avatar" :src="m.avatar" alt="Avatar" />
            <span v-else>{{ initials(m.nombre) }}</span>
          </div>
          <div class="headings">
            <h3>{{ m.nombre }}</h3>
            <p class="role" v-if="m.rol">{{ m.rol }}</p>
            <p class="muted" v-else>Rol no especificado</p>
          </div>
        </div>

        <p class="bio" v-if="m.bio">{{ m.bio }}</p>
        <p class="bio muted" v-else>Sin bio.</p>

        <ul v-if="m.skills?.length" class="skills">
          <li v-for="s in m.skills" :key="s">{{ s }}</li>
        </ul>

        <div class="links">
          <a v-if="m.github" :href="m.github" target="_blank" rel="noopener" class="btn link">GitHub</a>
          <a v-if="m.linkedin" :href="m.linkedin" target="_blank" rel="noopener" class="btn link">LinkedIn</a>
          <a v-if="m.sitio" :href="m.sitio" target="_blank" rel="noopener" class="btn link">Sitio</a>
          <a v-if="m.email" :href="`mailto:${m.email}`" class="btn link">Email</a>
        </div>
      </article>
    </div>
  </section>
</template>

<style scoped>
/* Layout base */
.grupo {
  padding: 56px 22px;
  max-width: 1100px;
  margin-inline: auto;
}

.encabezado {
  text-align: center;
  margin-bottom: 24px;
}
.encabezado h2 {
  margin: 0 0 8px;
  font-size: 1.8rem;
}
.encabezado p {
  margin: 0;
  color: var(--muted, #6b7280);
}

/* Grid de tarjetas */
.grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
}
@media (max-width: 900px) {
  .grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (max-width: 640px) {
  .grid { grid-template-columns: 1fr; }
}

.card {
  background: var(--card, #ffffff);
  border: 1px solid rgba(0,0,0,.06);
  border-radius: 16px;
  padding: 18px;
  box-shadow: 0 8px 20px rgba(0,0,0,.06);
  display: flex;
  flex-direction: column;
  gap: 12px;
}

/* Cabecera de tarjeta */
.card-header {
  display: flex;
  align-items: center;
  gap: 12px;
}
.avatar {
  width: 54px;
  height: 54px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  background: #f3f4f6;
  color: #111827;
  font-weight: 700;
  letter-spacing: 0.5px;
  overflow: hidden;
  user-select: none;
}
.avatar img { width: 100%; height: 100%; object-fit: cover; }
.headings h3 { margin: 0; font-size: 1.1rem; }
.role { margin: 4px 0 0; color: #2563eb; font-weight: 600; }
.muted { color: #6b7280; }

.bio { margin: 6px 0 0; }

.skills {
  margin: 0;
  padding: 0;
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}
.skills li {
  font-size: .85rem;
  padding: 6px 10px;
  border-radius: 999px;
  border: 1px dashed rgba(0,0,0,.15);
}

/* Botones y links */
.links {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}
.btn {
  appearance: none;
  border: 1px solid rgba(0,0,0,.12);
  background: #fff;
  border-radius: 10px;
  padding: 8px 12px;
  cursor: pointer;
  font-size: .95rem;
  text-decoration: none;
}
.btn.link { display: inline-flex; align-items: center; justify-content: center; }
</style>
