<template>
  <section id="habilidades" class="habilidades">
    <div class="contenedor">
      <h2 class="titulo">Nuestras Habilidades</h2>
      <p class="subtitulo">Un vistazo a nuestro stack tecnológico y herramientas.</p>

      <div class="categorias-container">
        <div v-for="(categorySkills, category) in skills" :key="category" class="categoria">
          <h3 class="categoria-titulo">{{ category }}</h3>
          <div class="iconos-grid">
            <div v-for="skill in categorySkills" :key="skill.name" class="skill-item" :title="skill.name">
              <img :src="`https://skillicons.dev/icons?i=${skill.slug}&theme=dark`" :alt="skill.name" />
              <span>{{ skill.name }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "Habilidades",
  data() {
    return {
      skills: {
        'Frontend': [
          { name: 'Vue.js', slug: 'vuejs' },
          { name: 'React', slug: 'react' },
          { name: 'Svelte', slug: 'svelte' },
          { name: 'HTML5', slug: 'html' },
          { name: 'CSS3', slug: 'css' },
          { name: 'JavaScript', slug: 'javascript' },
          { name: 'TypeScript', slug: 'typescript' },
          { name: 'Tailwind CSS', slug: 'tailwindcss' },
        ],
        'Backend': [
          { name: 'Node.js', slug: 'nodejs' },
          { name: 'Express', slug: 'express' },
          { name: 'NestJS', slug: 'nestjs' },
          { name: 'Java', slug: 'java' },
        ],
        'Bases de Datos': [
          { name: 'MongoDB', slug: 'mongodb' },
          { name: 'PostgreSQL', slug: 'postgresql' },
          { name: 'MySQL', slug: 'mysql' },
        ],
        'Herramientas y Colaboración': [
          { name: 'Git', slug: 'git' },
          { name: 'Docker', slug: 'docker' },
          { name: 'Figma', slug: 'figma' },
          { name: 'Vite', slug: 'vite' },
          { name: 'Vitest', slug: 'vitest' },
        ]
      }
    };
  },
};
</script>

<style scoped>
.habilidades {
  background: #1a1a1a; /* Un fondo oscuro para resaltar los iconos */
  color: #f0f0f0;
  padding: 5rem 1.5rem;
  text-align: center;
}

.contenedor {
  max-width: 1000px;
  margin: 0 auto;
}

.titulo {
  font-size: 2.8rem;
  font-weight: 700;
  color: #42b883; /* Verde Vue */
  margin-bottom: 0.5rem;
}

.subtitulo {
  font-size: 1.2rem;
  color: #aaa;
  margin-bottom: 4rem;
}

.categorias-container {
  display: flex;
  flex-direction: column;
  gap: 3.5rem;
}

.categoria {
  background: #242424;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.categoria-titulo {
  font-size: 1.6rem;
  color: #42b883;
  margin-bottom: 2rem;
  text-align: left;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid #444;
}

.iconos-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(90px, 1fr));
  gap: 2rem 1.5rem;
  justify-content: center;
}

.skill-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.8rem;
  text-align: center;
  transition: transform 0.3s ease;
}

.skill-item:hover {
  transform: scale(1.1);
}

.skill-item img {
  width: 48px;
  height: 48px;
  filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.5));
}

.skill-item span {
  font-size: 0.9rem;
  color: #ccc;
  font-weight: 500;
}

@media (max-width: 600px) {
  .titulo {
    font-size: 2.2rem;
  }
  .iconos-grid {
    grid-template-columns: repeat(auto-fill, minmax(80px, 1fr));
  }
}
</style>

