<template>
  <div class="registro">
    <h1>Crea tu perfil anónimo</h1>
    <form @submit.prevent="validarRegistro">
      <div>
        <input v-model="usuario" type="text" placeholder="Alias (Ej: UsuarioFeliz123)">
        <p v-if="errorUsuario" class="error">El alias debe tener al menos 5 caracteres</p>
      </div>
      <div>
        <input v-model="email" type="email" placeholder="Correo electrónico">
      </div>
      <button type="submit">Empezar a compartir</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      usuario: '',
      email: '',
      errorUsuario: false
    }
  },
  methods: {
    validarRegistro() {
      this.errorUsuario = this.usuario.length < 5;
      if(!this.errorUsuario) {
        alert("¡Registro exitoso! Bienvenido al espacio seguro.");
        this.$router.push('/');
      }
    }
  }
}
</script>

<style scoped>
.registro { max-width: 400px; margin: auto; padding: 20px; background: white; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
input { display: block; width: 100%; margin: 10px 0; padding: 10px; box-sizing: border-box; }
.error { color: red; font-size: 0.8em; }
</style>