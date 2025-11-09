<script setup>
import { integrantes } from '@/data/integrantes.js'

const placeHolderAvatar = 'https://cdn.jsdelivr.net/gh/edent/SuperTinyIcons/images/svg/user.svg'
// Si preferís un placeholder local, podés poner: '/img/placeholder-user.png'
</script>

<template>
  <section id="integrantes" class="wrap">
    <header class="encabezado">
      <h2>Integrantes</h2>
      <p class="sub">Conocé al equipo de <strong>Rebelde_Bug</strong></p>
    </header>

    <div class="grid">
      <article
        v-for="p in integrantes"
        :key="p.id"
        class="card"
      >
        <div class="foto">
          <img
            :src="p.avatar && p.avatar.trim() !== '' ? p.avatar : placeHolderAvatar"
            :alt="`Foto de ${p.nombre}`"
            loading="lazy"
          />
        </div>

        <div class="contenido">
          <h3 class="nombre">{{ p.nombre }}</h3>
          <p class="rol">{{ p.rol }}</p>
          <p class="bio">{{ p.bio }}</p>

          <div class="contacto">
            <a v-if="p.email" class="link" :href="`mailto:${p.email}`" title="Enviar correo">
              📧 {{ p.email }}
            </a>
            <a v-if="p.telefono" class="link" :href="`tel:${p.telefono.replace(/\\s|\\(|\\)|-/g,'')}`" title="Llamar">
              📞 {{ p.telefono }}
            </a>
          </div>
        </div>
      </article>
    </div>
  </section>
</template>

<style scoped>
/* Sección */
.wrap {
  padding: 4rem 1.5rem;
  background: var(--color-bg);           /* Fondo claro */
  color: var(--color-text);
}
.encabezado {
  text-align: center;
  margin-bottom: 3rem;
}
.encabezado h2 {
  font-size: 2.2rem;
  font-weight: 700;
  margin-bottom: .25rem;
  color: var(--color-text);
}
.sub {
  color: var(--color-text-light);
  font-size: 1.1rem;
}

/* Grid responsivo */
.grid {
  display: grid;
  gap: 1.75rem;
  grid-template-columns: 1fr;
}
@media (min-width: 640px) {
  .grid { grid-template-columns: repeat(2, 1fr); }
}
@media (min-width: 1024px) {
  .grid { grid-template-columns: repeat(3, 1fr); }
}

/* Tarjeta */
.card {
  display: grid;
  grid-template-columns: 96px 1fr;
  gap: 1rem;
  align-items: center;
  background: var(--color-card);          /* Muy claro, contrasta con el fondo */
  border: 1px solid var(--color-text);
  border-radius: 16px;
  padding: 1.5rem;
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}
.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0,0,0,.05);
  border-color: var(--color-primary);
}

/* Foto */
.foto {
  width: 96px; 
  height: 96px;
  border-radius: 50%;
  overflow: hidden;
  background: var(--color-border);
  display: flex; 
  align-items: center; 
  justify-content: center;
}
.foto img {
  width: 100%; 
  height: 100%; 
  object-fit: cover;
}

/* Contenido */
.contenido { 
  min-width: 0; 
}

.nombre {
  font-size: 1.25rem;
  font-weight: 700;
  color: var(--color-text);
  margin: 0;
}
.rol {
  color: var(--color-primary);               /* Azul sobrio */
  font-weight: 600;
  margin: .25rem 0 0.75rem;
}
.bio {
  color: var(--color-text-light);
  line-height: 1.6;
  margin-bottom: 0.75rem;
}

/* Contacto */
.contacto {
  display: flex;
  gap: .75rem;
  flex-wrap: wrap;
}
.link {
  display: inline-flex;
  gap: .4rem;
  align-items: center;
  padding: .5rem .8rem;
  border: 1px solid var(--color-warm);
  border-radius: 10px;
  text-decoration: none;
  color: var(--color-text);
  background: transparent;
  transition: background-color .2s, border-color .2s, color .2s;
}
.link:hover {
  background: var(--color-primary);
  border-color: var(--color-primary);
  color: #fff;
}
</style>
