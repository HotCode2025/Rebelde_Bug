<template>
  <section class="proyectos">
    <h1>Proyectos del Grupo</h1>
    <div class="lista-proyectos">
      <div v-for="(p, i) in proyectos" :key="i" class="proyecto-fila" :class="{ 'fila-inversa': i % 2 !== 0 }">
        <div class="proyecto-imagen-contenedor">
          <img :src="p.imagen" :alt="'Imagen de ' + p.nombre" class="proyecto-imagen">
        </div>
        <div class="proyecto-texto">
          <h3>{{ p.nombre }}</h3>
          <p>{{ p.descripcion }}</p>
        </div>
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
        {
          nombre: 'Creación de Portafolios Web',
          descripcion: 'Desarrollo de portafolios web personales y grupales utilizando tecnologías modernas como Vue.js y Vite. Diseño responsive y optimizado para SEO.',
          imagen: '/img/portafolio.jpeg'
        },
        {
          nombre: 'Juego del Ahorcado en Java',
          descripcion: 'Implementación del clásico juego del ahorcado con interfaz gráfica en Java Swing. El proyecto integra lógica de juego, gestión de palabras y puntuaciones.',
          imagen: '/img/juegoD.jpeg'
        },
        {
          nombre: 'App de Escritorio "TaskMaster"',
          descripcion: 'Aplicación de gestión de tareas para escritorio construida con Electron y Vue.js. Permite a los usuarios organizar sus actividades diarias, establecer prioridades y recibir notificaciones.',
          imagen: '/img/task.jpeg'
        }
      ],
    }
  },
}
</script>

<style scoped>
.proyectos {
  padding: 3rem 2rem;
  background-color: #fff;
}
.proyectos h1 {
  text-align: center;
  margin-bottom: 3rem;
  font-size: 2.5rem;
  color: #333;
}
.lista-proyectos {
  display: flex;
  flex-direction: column;
  gap: 3rem;
  max-width: 900px;
  margin: 0 auto;
}
.proyecto-fila {
  display: flex;
  align-items: center;
  gap: 2.5rem;
  background-color: #f9f9f9;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 6px 12px rgba(0,0,0,0.08);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.proyecto-fila:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 24px rgba(0,0,0,0.12);
}
.proyecto-fila.fila-inversa {
  flex-direction: row-reverse;
}
.proyecto-imagen-contenedor {
  flex: 1;
  max-width: 400px;
}
.proyecto-imagen {
  width: 100%;
  border-radius: 8px;
  display: block;
}
.proyecto-texto {
  flex: 1;
}
.proyecto-texto h3 {
  margin-bottom: 1rem;
  font-size: 1.8rem;
  color: #2c3e50;
}
.proyecto-texto p {
  color: #555;
  line-height: 1.6;
}
</style>
