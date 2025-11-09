<template>
  <section class="contacto">
    <h1>Contacto</h1>
    <form @submit.prevent="enviarFormulario">
      <input type="text" v-model="nombre" placeholder="Tu nombre" required />
      <input type="email" v-model="email" placeholder="Tu correo" required />
      <textarea v-model="mensaje" placeholder="Tu mensaje" required></textarea>
      <button type="submit">Enviar</button>
    </form>

    <p v-if="enviado" class="exito">¡Gracias por tu mensaje!</p>
  </section>
</template>

<script>
export default {
  name: 'Contacto',
  data() {
    return {
      nombre: '',
      email: '',
      mensaje: '',
      enviado: false,
    }
  },
  methods: {
    enviarFormulario() {
      // Por ahora solo mostramos un mensaje. Más adelante se puede conectar con un backend o un servicio de correo.
      this.enviado = true
      this.nombre = ''
      this.email = ''
      this.mensaje = ''
      setTimeout(() => (this.enviado = false), 3000)
    },
  },
}
</script>

<style scoped>
.contacto {
  padding: 2rem;
  text-align: center;
  max-width: 500px;
  margin: auto;
}
form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
input, textarea {
  padding: 0.8rem;
  border: 1px solid #ccc;
  border-radius: 6px;
}
button {
  background: #42b983;
  color: white;
  border: none;
  border-radius: 6px;
  padding: 0.8rem;
  cursor: pointer;
}
button:hover {
  background: #36a773;
}
.exito {
  margin-top: 1rem;
  color: #42b983;
  font-weight: bold;
}
</style>
