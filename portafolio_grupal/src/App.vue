<script setup>
import NavBar from './components/NavBar.vue'
import DatosIntegrantes from './components/DatosIntegrantes.vue'
</script>

<template>
  <header>
    <NavBar />
  </header>

  <main>
    <DatosIntegrantes />
  </main>
</template>

<style>
:root{
  --bg: #eef2f7;         /* fondo general */
  --bg-2: #e9edf3;       /* degradado suave */
  --text: #111827;       /* texto principal */
  --muted: #6b7280;      /* texto secundario */
  --card: #ffffff;       /* fondo tarjeta */
  --primary: #618faa;    /* color marca */
  --border: #e5e7eb;     /* bordes sutiles */
  --shadow-sm: 0 4px 12px rgba(0,0,0,.06);
  --shadow-md: 0 8px 20px rgba(0,0,0,.08);
}

html, body, #app { height: 100%; }
body{
  margin: 0;
  color: var(--text);
  background: linear-gradient(180deg, var(--bg), var(--bg-2));
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
:root { scroll-behavior: smooth; } /* anchors suaves */
</style>
