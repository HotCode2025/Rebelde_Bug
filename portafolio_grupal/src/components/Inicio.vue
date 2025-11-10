<script setup>
// Nada de lógica, solo presentación
import icono1 from '../assets/bug-preview.png';
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

      <!--<a href="#integrantes" class="boton">Conocé al equipo</a>-->
      <a class="boton" @click="() => $emit('change', 'integrantes')">Conocé al equipo</a>
    </div>

    <div class="decoracion">
      <img :src="icono1" alt="Icono grupo" />
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
  background: radial-gradient(circle at center, var(--color-bg-alt) 0%, var(--color-bg) 100%);
  color: var(--color-text);
  overflow: hidden;
  position: relative;
}

.contenido {
  max-width: 800px;
  padding: 1.5rem;
  z-index: 2;
}

.titulo {
  font-family: 'Orbitron', sans-serif;
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 1.2rem;
  color: var(--color-primary);
  text-shadow: 0 0 10px rgba(155, 92, 255, 0.6);
}

.resaltado {
  color: var(--color-secondary);
  text-shadow: 0 0 10px var(--color-secondary);
}

.descripcion {
  font-size: 1.1rem;
  line-height: 1.8;
  color: var(--color-subtext);
  margin-bottom: 1.2rem;
}

.boton {
  display: inline-block;
  margin-top: 2rem;
  padding: 0.9rem 2rem;
  font-size: 1rem;
  font-weight: 600;
  background: var(--color-primary);
  color: var(--color-bg);
  border-radius: 0.8rem;
  text-decoration: none;
  letter-spacing: 0.5px;
  transition: all 0.3s ease;
  box-shadow: 0 0 15px rgba(155, 92, 255, 0.5);
}

.boton:hover {
  background: var(--color-secondary);
  color: var(--color-bg);
  box-shadow: 0 0 20px var(--color-secondary);
  transform: translateY(-3px);
}

.decoracion {
  margin-top: 2rem;
  transform: translateY(-20px);
}

.decoracion img {
  width: 120px;
  opacity: 0.8;
  filter: drop-shadow(0 0 10px var(--color-tertiary));
  transition: transform 0.3s ease, filter 0.3s ease;
}

.decoracion img:hover {
  transform: scale(1.1) rotate(5deg);
  filter: drop-shadow(0 0 20px var(--color-secondary));
}

.inicio::before {
  content: "";
  position: absolute;
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(155, 92, 255, 0.15), transparent 70%);
  top: -100px;
  left: -100px;
  z-index: 0;
}

@media (max-width: 768px) {
  .titulo {
    font-size: 2.3rem;
  }
  .descripcion {
    font-size: 1rem;
  }
  .boton {
    padding: 0.8rem 1.6rem;
    font-size: 0.95rem;
  }
}

@media (max-width: 480px) {
  .titulo {
    font-size: 1.8rem;
  }
  .decoracion img {
    width: 90px;
  }
}
</style>
