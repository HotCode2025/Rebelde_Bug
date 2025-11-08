<template>
  <section class="habilidades">
    <h1>Habilidades</h1>
    <ul>
      <li v-for="(hab, index) in habilidades" :key="index">
        {{ hab }}
      </li>
    </ul>
  </section>
</template>

<script>
export default {
  name: 'Habilidades',
  data() {
    return {
      habilidades: [
        'HTML, CSS y JavaScript',
        'Vue.js y Vite',
        'Python básico',
        'Trabajo en equipo y comunicación',
      ],
    }
  },
}
</script>

<style scoped>
.habilidades {
  padding: 2rem;
  text-align: center;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  background: #f3f3f3;
  margin: 0.5rem auto;
  padding: 0.8rem 1rem;
  width: fit-content;
  border-radius: 8px;
}
</style>
