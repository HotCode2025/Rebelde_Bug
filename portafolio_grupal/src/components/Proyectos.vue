<template>
  <section class="proyectos">
    <h1>Mis Proyectos</h1>
    <div class="lista-proyectos">
      <div v-for="(p, i) in proyectos" :key="i" class="proyecto">
        <h3>{{ p.nombre }}</h3>
        <p>{{ p.descripcion }}</p>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Proyectos',
  data() {
    return {
      proyectos: [
        { nombre: 'Portfolio personal', descripcion: 'Sitio web con mis trabajos y contacto.' },
        { nombre: 'Gestor de tareas', descripcion: 'Aplicación para organizar actividades diarias.' },
      ],
    }
  },
}
</script>

<style scoped>
.proyectos {
  padding: 2rem;
}
.lista-proyectos {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}
.proyecto {
  border: 1px solid #ccc;
  border-radius: 10px;
  padding: 1rem;
  width: 250px;
}
</style>
