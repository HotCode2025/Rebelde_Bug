<template>
  <section id="intereses" class="intereses">
    <div class="stars">
      <div class="star"></div>
      <div class="star"></div>
      <div class="star"></div>
      <div class="star"></div>
      <div class="star"></div>
    </div>
    <div class="contenedor">
      <h2 class="titulo">Nuestros Intereses</h2>
      <div class="contenido">
        <p>
          Más allá del código, somos un grupo que valora la colaboración y el buen ambiente. Creemos que las mejores ideas surgen cuando hay confianza y compañerismo, por eso nos encanta juntarnos a compartir una buena comida y planificar nuestros próximos desafíos.
        </p>
        <p>
          Nuestra pasión es el desarrollo web. Organizamos sesiones de programación para explorar nuevas tecnologías, depurar código en equipo y construir proyectos como este portafolio. Nos entusiasma especialmente el ecosistema de JavaScript y las posibilidades que ofrecen frameworks modernos como Vue.js y React.
        </p>
        <p>
          Mirando hacia el futuro, aspiramos a aplicar nuestras habilidades en proyectos que tengan un impacto real. Nos interesa el desarrollo de aplicaciones interactivas, la visualización de datos y la creación de experiencias de usuario que sean tanto funcionales como atractivas. ¡Siempre estamos en busca de aprender y crecer!
        </p>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "Intereses",
};
</script>

<style scoped>
@keyframes anim-star {
  from {
    transform: translateY(0px);
  }
  to {
    transform: translateY(-2000px);
  }
}

@keyframes anim-shooting-star {
  from {
    transform: translateX(-300px) rotate(315deg);
  }
  to {
    transform: translateX(120vw) rotate(315deg);
  }
}

.intereses {
  background: radial-gradient(ellipse at bottom, #1b2735 0%, #090a0f 100%);
  color: #f0f0f0;
  padding: 5rem 1.5rem;
  text-align: center;
  position: relative;
  overflow: hidden;
  min-height: 80vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.stars {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  height: 100%;
  display: block;
}

/* Shooting Stars */
.stars::before, .stars::after {
  content: '';
  position: absolute;
  left: -100px;
  width: 150px;
  height: 1px;
  background: linear-gradient(to right, #FFF, rgba(255,255,255,0));
  animation: anim-shooting-star 12s linear infinite;
  border-radius: 50%;
  box-shadow: 0 0 8px #FFF;
}

.stars::before {
  top: 20vh;
  animation-delay: 5s;
}

.stars::after {
  top: 60vh;
  width: 200px;
  height: 2px;
  animation-duration: 8s;
  animation-delay: 1s;
}


.star {
  position: absolute;
  top: 0;
  left: 0;
  width: 1px;
  height: 1px;
  background: white;
  animation: anim-star 150s linear infinite;
}

.star:nth-child(2) {
  width: 2px;
  height: 2px;
  animation-duration: 100s;
  animation-delay: -30s;
}

.star:nth-child(3) {
  width: 1px;
  height: 1px;
  animation-duration: 80s;
  animation-delay: -50s;
}

.star:nth-child(4) {
  width: 2px;
  height: 2px;
  animation-duration: 60s;
  animation-delay: -10s;
}

.star:nth-child(5) {
  width: 1px;
  height: 1px;
  animation-duration: 90s;
  animation-delay: -100s;
}

/* Generar estrellas aleatorias */
.star:nth-child(1) { box-shadow: 50vw 80vh 1px 1px #FFF, 10vw 30vh 1px 1px #FFF, 90vw 10vh 2px 2px #FFF; }
.star:nth-child(2) { box-shadow: 20vw 50vh 2px 2px #FFF, 70vw 90vh 1px 1px #FFF, 40vw 20vh 1px 1px #FFF; }
.star:nth-child(3) { box-shadow: 80vw 60vh 1px 1px #FFF, 30vw 10vh 2px 2px #FFF, 5vw 70vh 1px 1px #FFF; }
.star:nth-child(4) { box-shadow: 60vw 40vh 2px 2px #FFF, 95vw 85vh 1px 1px #FFF, 25vw 5vh 1px 1px #FFF; }
.star:nth-child(5) { box-shadow: 15vw 65vh 1px 1px #FFF, 85vw 25vh 2px 2px #FFF, 55vw 95vh 1px 1px #FFF; }


.contenedor {
  max-width: 800px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
  background: rgba(27, 39, 53, 0.5);
  padding: 2.5rem;
  border-radius: 15px;
  backdrop-filter: blur(5px);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.titulo {
  font-size: 2.8rem;
  font-weight: 700;
  color: #42b883;
  margin-bottom: 2rem;
}

.contenido p {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #ccc;
  margin-bottom: 1.5rem;
}

.contenido p:last-child {
  margin-bottom: 0;
}
</style>