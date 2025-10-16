<script setup>
// Nada de lógica, solo presentación
</script>

<template>
  <section class="inicio">
    <div class="contenido">
      <h1 class="titulo">
        Somos el grupo <span class="resaltado">Rebelde_Bug</span>
      </h1>

      <p class="descripcion">
        Estudiantes de la <strong>Universidad Tecnológica Nacional (UTN)</strong>, apasionados por la programación,
        el aprendizaje constante y el trabajo colaborativo.
      </p>

      <p class="descripcion">
        Nos motiva crear proyectos que nos reten, aprender nuevas tecnologías y mejorar como equipo en cada práctica.
        Creemos que la mejor forma de crecer es compartiendo conocimientos y experiencias.
      </p>

      <a href="#integrantes" class="boton">Conocé al equipo</a>
    </div>

    <div class="decoracion">
      <img src="https://cdn-icons-png.flaticon.com/512/616/616408.png" alt="Icono grupo" />
    </div>
  </section>
</template>

<style scoped>
.inicio {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  min-height: 90vh;
  padding: 2rem;
  background-color: #f9fafb; /* Fondo claro */
  color: #333;
}

.contenido {
  max-width: 800px;
  padding: 1.5rem;
}

.titulo {
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 1rem;
  color: #222;
}

.resaltado {
  color: #0077cc;
}

.descripcion {
  font-size: 1.15rem;
  line-height: 1.6;
  color: #555;
  margin-bottom: 1rem;
}

.boton {
  display: inline-block;
  margin-top: 1.5rem;
  padding: 0.8rem 1.8rem;
  font-size: 1rem;
  font-weight: 600;
  background-color: #0077cc;
  color: white;
  border-radius: 0.6rem;
  text-decoration: none;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.boton:hover {
  background-color: #005fa3;
  transform: scale(1.03);
}

.decoracion {
  margin-top: 2rem;
}

.decoracion img {
  width: 100px;
  opacity: 0.8;
}
</style>
