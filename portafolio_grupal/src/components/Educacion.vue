<script setup>
import { educacion } from "@/data/educacion.js";

// Asignamos íconos según el tipo de evento (por año o título)
const iconos = {
  2025: "🚀",
  2024: "💻",
  2023: "🎓",
  2022: "🧠",
  "2020 - 2021": "🤝",
};
</script>

<template>
  <section id="educacion" class="educacion-wrap">
    <header class="header">
      <h2>Formación del grupo</h2>
      <p>Un recorrido compartido de aprendizaje, colaboración y crecimiento</p>
    </header>

    <div class="timeline">
      <div
        v-for="(item, index) in educacion"
        :key="index"
        class="timeline-item"
      >
        <div class="timeline-icon">
          {{ iconos[item.anio] || "🎓" }}
        </div>
        <div class="timeline-content">
          <div class="timeline-year">{{ item.anio }}</div>
          <h3 class="timeline-title">{{ item.titulo }}</h3>
          <h4 class="timeline-inst">{{ item.institucion }}</h4>
          <p class="timeline-desc">{{ item.descripcion }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.educacion-wrap {
  background: #f9fafb;
  color: #333;
  padding: 3rem 1.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* encabezado */
.header {
  text-align: center;
  margin-bottom: 2.5rem;
}
.header h2 {
  font-size: 2rem;
  font-weight: 700;
  color: #0a2a4d;
}
.header p {
  color: #6b7280;
  font-size: 1rem;
  margin-top: 0.25rem;
}

/* línea de tiempo */
.timeline {
  position: relative;
  max-width: 760px;
  width: 100%;
  margin: 0 auto;
  padding-left: 2.2rem;
  border-left: 3px solid #0077cc;
}

.timeline-item {
  position: relative;
  margin-bottom: 2rem;
  transition: transform 0.2s ease;
}
.timeline-item:hover {
  transform: translateY(-4px);
}

/* icono */
.timeline-icon {
  position: absolute;
  left: -38px;
  top: 10px;
  background: #ffffff;
  border: 3px solid #0077cc;
  color: #0077cc;
  width: 42px;
  height: 42px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);
}

/* contenido */
.timeline-content {
  background: #ffffff;
  border-radius: 10px;
  padding: 1rem 1.25rem 1.25rem 1.25rem;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.07);
  transition: box-shadow 0.3s ease;
}
.timeline-item:hover .timeline-content {
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1);
}

.timeline-year {
  color: #0077cc;
  font-weight: 700;
  font-size: 1rem;
  margin-bottom: 0.3rem;
}

.timeline-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: #111827;
  margin-bottom: 0.3rem;
}

.timeline-inst {
  font-size: 1rem;
  font-weight: 500;
  color: #374151;
  margin-bottom: 0.6rem;
}

.timeline-desc {
  font-size: 0.95rem;
  color: #555;
  line-height: 1.55;
}

/* efecto de línea */
.timeline::before {
  content: "";
  position: absolute;
  left: -2px;
  top: 0;
  height: 100%;
  width: 3px;
  background: linear-gradient(#0077cc, #00b4d8);
  border-radius: 2px;
}
</style>
