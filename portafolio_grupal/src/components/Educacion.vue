<!-- src/components/Educacion.vue -->
<script setup>
import { computed } from "vue";
import { integrantes } from "@/data/integrantes.js";
import { educacion as EDU } from "@/data/educacion.js";

/** Merge por id y construir una línea de tiempo por integrante */
function parseDate(s) {
  if (!s) return null;
  // acepta "YYYY" o "YYYY-MM"
  const m = String(s).match(/^(\d{4})(?:-(\d{2}))?$/);
  if (!m) return null;
  const y = Number(m[1]);
  const mo = Number(m[2] || "01");
  return { y, mo };
}
function dateToNum(d) {
  if (!d) return -Infinity;
  return d.y * 100 + d.mo; // 2024-09 -> 202409
}

const merged = computed(() => {
  const byId = new Map(EDU.map(e => [e.id, e]));
  return integrantes
    .map(p => {
      const e = byId.get(p.id) || { formacion: [], certificaciones: [] };
      // construir items de timeline:
      const timeline = [];

      // Formación (bloques que pueden tener desde/hasta)
      for (const f of e.formacion || []) {
        const desde = parseDate(f.desde);
        const hasta = f.hasta && f.hasta.toLowerCase?.() === "actualidad"
          ? { y: 9999, mo: 12 }
          : parseDate(f.hasta) || desde;
        timeline.push({
          tipo: "formacion",
          titulo: f.titulo,
          subtitulo: f.institucion,
          nivel: f.nivel,
          estado: f.estado,
          desde,
          hasta,
          link: f.link || "",
          // clave de orden: fin (hasta) primero, luego inicio
          orderKey: dateToNum(hasta) * 10000 + dateToNum(desde)
        });
      }

      // Certificaciones (punto en el tiempo -> usar anio como desde/hasta)
      for (const c of e.certificaciones || []) {
        const d = parseDate(String(c.anio || ""));
        timeline.push({
          tipo: "certificacion",
          titulo: c.nombre,
          subtitulo: c.entidad,
          nivel: "Certificación",
          estado: "",
          desde: d,
          hasta: d,
          link: c.link || "",
          orderKey: dateToNum(d)
        });
      }

      // Orden descendente (más reciente arriba)
      timeline.sort((a, b) => b.orderKey - a.orderKey);

      return { ...p, timeline };
    })
    .sort((a, b) => a.nombre.localeCompare(b.nombre));
});

function fmtPeriodo(it) {
  const fmt = (d) => (d ? `${d.y}${d.mo ? '-' + String(d.mo).padStart(2,'0') : ''}` : '');
  const d = fmt(it.desde);
  const h = it.hasta?.y === 9999 ? "Actualidad" : fmt(it.hasta);
  if (d && h && d !== h) return `${d} – ${h}`;
  return d || h || "";
}
function initials(name) {
  return name
    .split(" ").filter(Boolean).slice(0, 2)
    .map(w => w[0]?.toUpperCase()).join("");
}
</script>

<template>
  <section class="educacion">
    <header class="encabezado">
      <h2>Educación</h2>
      <p>Editá <code>src/data/educacion.js</code> para agregar <strong>formación</strong> y <strong>certificaciones</strong>.</p>
      <p class="hint">Formato de fechas aceptado: <code>YYYY</code> o <code>YYYY-MM</code>. Usá <code>Actualidad</code> en <em>hasta</em> si seguís cursando.</p>
    </header>

    <div class="grid">
      <article v-for="m in merged" :key="m.id" class="card">
        <div class="card-header">
          <div class="avatar" :title="m.nombre">
            <img v-if="m.avatar" :src="m.avatar" alt="Avatar" />
            <span v-else>{{ initials(m.nombre) }}</span>
          </div>
          <div class="headings">
            <h3>{{ m.nombre }}</h3>
            <p class="muted" v-if="m.rol">{{ m.rol }}</p>
          </div>
        </div>

        <div v-if="m.timeline.length" class="timeline">
          <div v-for="(it, i) in m.timeline" :key="i" class="t-item">
            <div class="t-point" :class="it.tipo"></div>
            <div class="t-content">
              <div class="t-header">
                <span class="t-badge" :class="it.tipo">
                  {{ it.tipo === 'formacion' ? (it.nivel || 'Formación') : 'Certificación' }}
                </span>
                <span class="t-period">{{ fmtPeriodo(it) }}</span>
              </div>
              <div class="t-title">{{ it.titulo }}</div>
              <div class="t-sub">{{ it.subtitulo }}</div>
              <div class="t-meta">
                <span v-if="it.estado" class="chip">{{ it.estado }}</span>
                <a v-if="it.link" class="ext" :href="it.link" target="_blank" rel="noopener">Ver más</a>
              </div>
            </div>
          </div>
        </div>
        <p v-else class="muted">Sin educación/certificaciones cargadas.</p>
      </article>
    </div>
  </section>
</template>

<style scoped>
.educacion { padding: 56px 22px; max-width: 1100px; margin-inline: auto; }
.encabezado { text-align: center; margin-bottom: 24px; }
.encabezado h2 { margin: 0 0 8px; font-size: 1.8rem; }
.encabezado p { margin: 0; color: var(--muted, #6b7280); }
.hint { font-size: .9rem; margin-top: 6px; }

.grid { display: grid; grid-template-columns: 1fr; gap: 16px; }
.card {
  background: var(--card, #ffffff);
  border: 1px solid rgba(0,0,0,.06);
  border-radius: 16px;
  padding: 18px;
  box-shadow: 0 8px 20px rgba(0,0,0,.06);
}

.card-header { display: flex; align-items: center; gap: 12px; margin-bottom: 6px; }
.avatar {
  width: 54px; height: 54px; border-radius: 50%; display: grid; place-items: center;
  background: #f3f4f6; color: #111827; font-weight: 700; overflow: hidden; user-select: none;
}
.avatar img { width: 100%; height: 100%; object-fit: cover; }
.headings h3 { margin: 0; font-size: 1.1rem; }
.muted { color: #6b7280; }

/* Timeline */
.timeline { position: relative; padding-left: 26px; margin-top: 10px; }
.timeline::before {
  content: ""; position: absolute; left: 10px; top: 0; bottom: 0;
  width: 2px; background: linear-gradient(to bottom, #e5e7eb, #e5e7eb);
}
.t-item { position: relative; margin: 16px 0; }
.t-point {
  position: absolute; left: 2px; top: .55rem;
  width: 16px; height: 16px; border-radius: 50%; border: 2px solid #fff;
  box-shadow: 0 0 0 2px rgba(0,0,0,.08);
  background: #9ca3af;
}
.t-point.formacion { background: #3b82f6; }
.t-point.certificacion { background: #10b981; }

.t-content { background: #fff; border: 1px solid rgba(0,0,0,.06); border-radius: 12px; padding: 10px 12px; }
.t-header { display: flex; align-items: center; justify-content: space-between; gap: 8px; }
.t-badge {
  font-size: .8rem; padding: 2px 8px; border-radius: 999px; border: 1px solid rgba(0,0,0,.08);
  background: #f9fafb;
}
.t-badge.formacion { background: #eff6ff; border-color: #bfdbfe; color: #1d4ed8; }
.t-badge.certificacion { background: #ecfdf5; border-color: #a7f3d0; color: #047857; }
.t-period { font-size: .85rem; color: #374151; }

.t-title { font-weight: 700; margin-top: 4px; }
.t-sub { color: #4b5563; }
.t-meta { display: flex; gap: 8px; align-items: center; margin-top: 6px; }
.chip { font-size: .75rem; padding: 2px 8px; border-radius: 999px; border: 1px solid rgba(0,0,0,.12); }
.ext { text-decoration: none; font-size: .9rem; border: 1px solid rgba(0,0,0,.12); padding: 2px 8px; border-radius: 8px; }
</style>
