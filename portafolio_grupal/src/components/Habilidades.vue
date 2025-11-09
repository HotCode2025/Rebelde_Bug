<template>
  <section id="habilidades" class="habilidades">
    <div class="contenedor">
      <h2 class="titulo">Habilidades</h2>
      <p class="subtitulo">Tecnologías y fortalezas del equipo</p>

      <ul class="lista">
        <li v-for="(hab, index) in habilidades" :key="index" class="item">
          <span class="bullet">⚡</span> {{ hab }}
        </li>
      </ul>
    </div>
  </section>
</template>

<script>
export default {
  name: "Habilidades",
  data() {
    return {
      habilidades: [
        "HTML, CSS y JavaScript",
        "Vue.js y Vite",
        "Python básico",
        "Trabajo en equipo y comunicación",
      ],
    };
  },
};
</script>

<style scoped>
.habilidades {
  background: var(--color-bg);
  color: var(--color-text);
  padding: 4rem 1.5rem;
  text-align: center;
}

.contenedor {
  max-width: 900px;
  margin: 0 auto;
}

/* ===== Títulos ===== */
.titulo {
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--color-primary);
  margin-bottom: 0.5rem;
}

.subtitulo {
  font-size: 1.1rem;
  color: var(--color-subtext);
  margin-bottom: 2rem;
}

/* ===== Lista ===== */
.lista {
  display: grid;
  gap: 1rem;
  justify-content: center;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  padding: 0;
  list-style: none;
}

.item {
  background: var(--color-bg-alt);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-left: 4px solid var(--color-secondary);
  padding: 1rem 1.25rem;
  border-radius: 10px;
  font-size: 1.1rem;
  color: var(--color-text);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.6rem;
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}

.item:hover {
  transform: translateY(-4px);
  border-color: var(--color-tertiary);
  box-shadow: 0 0 12px var(--color-secondary);
}

.bullet {
  color: var(--color-secondary);
  font-size: 1.3rem;
}

/* ===== Responsividad ===== */
@media (max-width: 600px) {
  .titulo {
    font-size: 2rem;
  }
  .item {
    font-size: 1rem;
    padding: 0.9rem 1rem;
  }
}
</style>
