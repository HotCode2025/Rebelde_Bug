<!-- src/components/DatosIntegrantes.vue -->
<script setup>
import { computed } from "vue";
import { integrantes as RAW } from "@/data/integrantes.js";

const integrantes = computed(() =>
  [...RAW].sort((a, b) => a.nombre.localeCompare(b.nombre))
);

function initials(name) {
  return name
    .split(" ")
    .filter(Boolean)
    .slice(0, 2)
    .map((w) => w[0]?.toUpperCase())
    .join("");
}
</script>

<template>
  <section class="integrantes">
    <header class="encabezado">
      <h2>Integrantes</h2>
      <p class="sub">Conocé al equipo y sus habilidades.</p>
    </header>

    <div class="grid">
      <article v-for="m in integrantes" :key="m.id" class="card">
        <div class="header">
          <div class="avatar" :title="m.nombre">
            <img v-if="m.avatar" :src="m.avatar" alt="Avatar" />
            <span v-else>{{ initials(m.nombre) }}</span>
          </div>

          <div class="titles">
            <h3 class="name">{{ m.nombre }}</h3>
            <a v-if="m.rol" class="role" href="javascript:void(0)">{{ m.rol }}</a>
            <span v-else class="role muted">Rol no especificado</span>
          </div>
        </div>

        <p class="bio" v-if="m.bio">{{ m.bio }}</p>
        <p class="bio muted" v-else>Sin bio todavía.</p>

        <ul v-if="m.skills?.length" class="skills">
          <li v-for="s in m.skills" :key="s" class="chip">{{ s }}</li>
        </ul>

        <div class="links">
          <a v-if="m.github" :href="m.github" target="_blank" rel="noopener" class="btn ghost">GitHub</a>
          <a v-if="m.linkedin" :href="m.linkedin" target="_blank" rel="noopener" class="btn ghost">LinkedIn</a>
          <a v-if="m.sitio" :href="m.sitio" target="_blank" rel="noopener" class="btn ghost">Sitio</a>
          <a v-if="m.email" :href="`mailto:${m.email}`" class="btn">Email</a>
        </div>
      </article>
    </div>
  </section>
</template>

<style scoped>
.integrantes{
  padding: 36px 22px 56px;
  max-width: 1200px;
  margin-inline: auto;
}
.encabezado{
  text-align:center; margin-bottom: 22px;
}
.encabezado h2{
  margin:0;
  font-size: clamp(1.6rem, 2.4vw, 2rem);
}
.sub{ color:#6b7280; margin:4px 0 0; }

.grid{
  display:grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
}
@media (max-width: 980px){ .grid{ grid-template-columns: repeat(2, minmax(0,1fr)); } }
@media (max-width: 640px){ .grid{ grid-template-columns: 1fr; } }

.card{
  background:#ffffff;
  border:1px solid rgba(0,0,0,.06);
  border-radius: 18px;
  padding: 18px;
  box-shadow: 0 10px 24px rgba(15,23,42,.06);
  transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease;
}
.card:hover{
  transform: translateY(-3px);
  box-shadow: 0 16px 36px rgba(15,23,42,.10);
  border-color: rgba(0,0,0,.10);
}

.header{
  display:flex; align-items:center; gap:12px; margin-bottom: 8px;
}

.avatar{
  width: 54px; height: 54px; border-radius: 50%;
  display:grid; place-items:center; overflow:hidden; position:relative;
  background: #f1f5f9; color:#0f172a; font-weight:800; letter-spacing:.4px;
}
.avatar::after{
  /* anillo degradado suave */
  content:""; position:absolute; inset:-2px; border-radius:50%;
  background: conic-gradient(from 180deg, #60a5fa, #a78bfa, #34d399, #60a5fa);
  z-index:-1; filter: blur(6px); opacity:.35;
}
.avatar img{ width:100%; height:100%; object-fit:cover; }

.name{ margin:0; font-size:1.05rem; }
.role{
  display:inline-block; margin-top:4px;
  color:#2563eb; text-decoration:none; font-weight:600;
  transition: color .15s ease;
}
.role:hover{ color:#1d4ed8; }
.muted{ color:#9ca3af; font-weight:500; }

.bio{ margin: 8px 0 0; color:#334155; }

.skills{
  margin: 10px 0 0; padding:0; list-style:none;
  display:flex; flex-wrap:wrap; gap:8px;
}
.chip{
  font-size:.85rem; padding:6px 10px; border-radius: 999px;
  background: #f1f5f9;
  border:1px dashed #e2e8f0;
  color:#0f172a;
}

.links{
  display:flex; flex-wrap:wrap; gap:8px; margin-top:12px;
}
.btn{
  appearance:none; cursor:pointer; text-decoration:none;
  border-radius: 10px; padding:8px 12px; font-size:.95rem;
  background:#111827; color:#fff; border:1px solid #111827;
  transition: transform .12s ease, box-shadow .12s ease, background .12s ease;
}
.btn:hover{ transform: translateY(-1px); box-shadow: 0 6px 16px rgba(17,24,39,.15); }
.btn.ghost{
  background:#fff; color:#0f172a; border:1px solid #e5e7eb;
}
.btn.ghost:hover{
  background:#f8fafc;
}
</style>
