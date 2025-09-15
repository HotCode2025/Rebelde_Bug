<script setup>
const integrantes = [
  'Camila Scheurer',
  'Zoé Geraldine Garnica',
  'Maximiliano Foglia',
  'Rubén Marchisio',
  'José Cueva',
  'Melina Denise Gallo',
  'Aramayo Micaela Cynthia',
  'Ivana Daniela Molina',
  'Jimena Karin Pérez',
]
</script>

<template>
  <section id="integrantes" class="grupo">
    <header class="encabezado">
      <h2>Integrantes – Rebelde Bug</h2>
      <p>Portafolio grupal con la misma estética del personal.</p>
    </header>

    <div class="grid">
      <div v-for="(n, idx) in integrantes" :key="idx" class="card">
        <h3 class="nombre">{{ n }}</h3>
        <p class="titulo">Estudiante UTN – Programación</p>
      </div>
    </div>
  </section>
</template>

<style scoped>
.grupo {
  padding: 56px 20px;
  border-top: 1px solid var(--border);
}
.encabezado {
  text-align: center;
  margin-bottom: 28px;
}
.encabezado h2 {
  margin: 0 0 6px;
  color: var(--text);
  font-size: 1.75rem;
  letter-spacing: .2px;
}
.encabezado p {
  margin: 0;
  color: var(--muted);
}

/* contenedor centrado y ancho máximo coherente con la navbar */
.grid {
  max-width: 1100px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 18px;
}

/* tarjetas */
.card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 18px 16px;
  box-shadow: var(--shadow-sm);
  transition: transform .15s ease, box-shadow .2s ease, border-color .2s ease;
}
.card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
  border-color: #d8dce2;
}
.nombre {
  margin: 0 0 6px;
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--text);
}
.titulo {
  margin: 0;
  color: var(--muted);
  font-size: .95rem;
  line-height: 1.5;
}

/* responsive fino */
@media (max-width: 768px) {
  .encabezado h2 { font-size: 1.45rem; }
  .grid { gap: 14px; }
}
@media (max-width: 480px) {
  .grupo { padding: 44px 14px; }
  .card { padding: 16px 14px; }
}
</style>