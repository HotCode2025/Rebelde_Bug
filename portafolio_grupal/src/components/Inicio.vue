<!-- src/components/Inicio.vue -->
<script setup>
import { defineEmits } from "vue";
const emit = defineEmits(["change"]);
function go(key){ emit("change", key); }
</script>

<template>
  <section class="hero">
    <div class="content">
      <h1>Portafolio Grupal</h1>
      <p class="lead">
        Proyecto del equipo UTN: integrando <strong>personas</strong>, <strong>habilidades</strong> y <strong>formación</strong> en un mismo sitio.
      </p>

      <div class="actions">
        <button class="btn primary" @click="go('integrantes')">Ver Integrantes</button>
        <button class="btn ghost" @click="go('educacion')">Ver Educación</button>
      </div>

      <div class="highlights">
        <div class="item">
          <div class="num">9</div>
          <div class="txt">Integrantes</div>
        </div>
        <div class="item">
          <div class="num">+30</div>
          <div class="txt">Skills</div>
        </div>
        <div class="item">
          <div class="num">∞</div>
          <div class="txt">Aprendizaje</div>
        </div>
      </div>
    </div>

    <div class="art">
      <!-- simple decorative block -->
      <div class="blob a"></div>
      <div class="blob b"></div>
      <div class="card">
        <h3>¿Qué vas a encontrar?</h3>
        <ul>
          <li>Tarjetas con bio, links y skills</li>
          <li>Formación y certificaciones por persona</li>
          <li>Estructura simple, todo desde el <code>repo</code></li>
        </ul>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero {
  display: grid;
  grid-template-columns: 1.1fr .9fr;
  gap: 24px;
  min-height: calc(100vh - 72px);
  padding: 36px 22px 56px;
  max-width: 1200px;
  margin-inline: auto;
}
@media (max-width: 980px){
  .hero { grid-template-columns: 1fr; align-items: center; }
  .art { order: -1; }
}

.content h1{
  margin: 0 0 8px;
  font-size: clamp(2rem, 4vw, 3rem);
  line-height: 1.05;
}
.lead{
  color: #4b5563;
  margin: 0 0 16px;
  max-width: 52ch;
}

.actions{ display: flex; gap: 10px; margin: 14px 0 28px; }
.btn{
  appearance: none; border-radius: 12px; padding: 12px 16px; cursor: pointer;
  font-size: 1rem; border: 1px solid rgba(0,0,0,.12); background: #fff;
}
.btn.primary{ background: #111827; color: #fff; border-color: #111827; }
.btn.ghost{ background: #fff; }

.highlights{
  display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; max-width: 520px;
}
.highlights .item{
  background: #fff; border: 1px solid rgba(0,0,0,.06); border-radius: 14px;
  padding: 14px; text-align: center; box-shadow: 0 10px 24px rgba(0,0,0,.04);
}
.num{ font-size: 1.6rem; font-weight: 800; }
.txt{ color:#6b7280; }

.art { position: relative; min-height: 300px; display: grid; place-items: center; }
.blob{
  position: absolute; width: 280px; height: 280px; border-radius: 50%;
  filter: blur(40px); opacity: .45;
}
.blob.a{ background: #60a5fa; top: 10%; left: 10%; }
.blob.b{ background: #34d399; bottom: 8%; right: 6%; }

.card{
  position: relative; background: #fff; border-radius: 16px; border:1px solid rgba(0,0,0,.08);
  padding: 18px; width: min(420px, 92%); box-shadow: 0 16px 40px rgba(0,0,0,.08);
}
.card h3{ margin: 0 0 10px; }
.card ul{ margin: 0; padding-left: 18px; color: #374151; }
</style>
