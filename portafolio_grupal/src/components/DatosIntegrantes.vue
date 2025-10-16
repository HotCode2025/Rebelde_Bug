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
  padding: 3rem 1.25rem;
  background: #ffffff;           /* Fondo claro */
  color: #333;
}
.encabezado {
  text-align: center;
  margin-bottom: 2rem;
}
.encabezado h2 {
  font-size: 2rem;
  margin-bottom: .25rem;
  color: #1f2937;
}
.sub {
  color: #6b7280;
  font-size: 1rem;
}

/* Grid responsivo */
.grid {
  display: grid;
  gap: 1.25rem;
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
  background: #f8fafc;          /* Muy claro, contrasta con el fondo */
  border: 1px solid #e5e7eb;
  border-radius: 14px;
  padding: 1rem;
  transition: transform .15s ease, box-shadow .15s ease, border-color .2s;
}
.card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 22px rgba(0,0,0,.06);
  border-color: #d1d5db;
}

/* Foto */
.foto {
  width: 96px; height: 96px;
  border-radius: 50%;
  overflow: hidden;
  background: #e5e7eb;
  display: flex; align-items: center; justify-content: center;
}
.foto img {
  width: 100%; height: 100%; object-fit: cover;
}

/* Contenido */
.contenido { min-width: 0; }
.nombre {
  font-size: 1.15rem;
  font-weight: 700;
  color: #111827;
  margin: 0;
}
.rol {
  color: #2563eb;               /* Azul sobrio */
  font-weight: 600;
  margin: .15rem 0 .5rem;
}
.bio {
  color: #4b5563;
  line-height: 1.5;
  margin-bottom: .75rem;
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
  padding: .5rem .7rem;
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  text-decoration: none;
  color: #374151;
  background: #fff;
  transition: background-color .2s, border-color .2s, color .2s;
}
.link:hover {
  background: #f3f4f6;
  border-color: #d1d5db;
  color: #111827;
}
</style>
