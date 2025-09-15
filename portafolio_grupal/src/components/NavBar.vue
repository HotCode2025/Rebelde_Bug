<script setup>
// Menú del portafolio grupal
const navegacion = [
  { nombre: 'Inicio', enlace: '#' },
  { nombre: 'Integrantes', enlace: '#integrantes' },
]
</script>

<template>
  <nav class="navbar" role="navigation" aria-label="Principal">
    <div class="navbar-container">
      <a class="brand" href="#">Rebelde Bug</a>
      <ul class="navbar-menu">
        <li v-for="(item, i) in navegacion" :key="i">
          <a :href="item.enlace" class="navbar-item">{{ item.nombre }}</a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  position: sticky;
  top: 0;
  z-index: 50;
  background: var(--primary);
  width: 100%;
  box-shadow: 0 2px 8px rgba(0,0,0,.08);
}

/* este container ahora ocupa toda la barra */
.navbar-container {
  width: 100%;
  max-width: 1300px;   /* aumenta el ancho máximo */
  margin: 0 auto;
  padding: 12px 24px;  /* más aire */
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.brand {
  color: #fff;
  font-weight: 700;
  text-decoration: none;
  font-size: 1.3rem;
  letter-spacing: .5px;
}

.navbar-menu {
  list-style: none;
  display: flex;
  gap: 20px;           /* más separación */
  margin: 0;
  padding: 0;
}

.navbar-item {
  color: #fff;
  text-decoration: none;
  font-weight: 500;
  padding: 10px 16px;  /* botones más grandes */
  border-radius: 8px;
  transition: background .2s ease, transform .12s ease;
}
.navbar-item:hover {
  background: rgba(0, 0, 0, 0.22);
  transform: translateY(-1px);
}

@media (max-width: 640px) {
  .navbar-container { flex-direction: column; align-items: flex-start; }
  .navbar-menu { flex-wrap: wrap; justify-content: center; width: 100%; }
}
</style>
