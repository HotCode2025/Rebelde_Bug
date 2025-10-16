<script setup>
import { experiencias } from "@/data/experiencia.js";
</script>

<template>
  <section id="experiencia" class="experiencia-wrap">
    <header class="header">
      <h2>Experiencias del grupo</h2>
      <p>Lo que aprendimos y construimos juntos</p>
    </header>

    <div class="cards">
      <article
        v-for="(item, index) in experiencias"
        :key="index"
        class="card"
      >
        <div class="icono">{{ item.icono }}</div>
        <div class="contenido">
          <h3 class="titulo">{{ item.titulo }}</h3>
          <p class="descripcion">{{ item.descripcion }}</p>
        </div>
      </article>
    </div>
  </section>
</template>

<style scoped>
.experiencia-wrap {
  background: #ffffff;
  color: #333;
  padding: 3rem 1.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* Encabezado */
.header {
  text-align: center;
  margin-bottom: 2.5rem;
}
.header h2 {
  font-size: 2rem;
  font-weight: 700;
  color: #0a2a4d;
}
.header p {
  color: #6b7280;
  font-size: 1rem;
  margin-top: 0.25rem;
}

/* Cards */
.cards {
  display: grid;
  gap: 1.5rem;
  grid-template-columns: 1fr;
  max-width: 900px;
}
@media (min-width: 768px) {
  .cards {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (min-width: 1024px) {
  .cards {
    grid-template-columns: repeat(3, 1fr);
  }
}

.card {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  transition: transform 0.2s ease, box-shadow 0.3s ease;
}
.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.08);
}

.icono {
  font-size: 2rem;
  margin-bottom: 0.5rem;
  color: #0077cc;
}

.titulo {
  font-size: 1.15rem;
  font-weight: 600;
  color: #111827;
  margin-bottom: 0.5rem;
}

.descripcion {
  font-size: 0.95rem;
  color: #4b5563;
  line-height: 1.5;
}
</style>
