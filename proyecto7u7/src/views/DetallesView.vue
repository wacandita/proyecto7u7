<template>
<div class="conteiner">
    <p v-if="loading">Cargando...</p>
    <p v-if="error">{{ error }}</p>

    <div v-if="psicologo" class="perfil">
        <img :src="psicologo.imagen" :alt="psicologo.nombre">

        <h1>{{ psicologo.nombre }}</h1>

        <p><strong>Descripción:</strong> {{ psicologo.descripcion }}</p>
        <p><strong>Ubicación:</strong> {{ psicologo.ubicacion }}</p>
        <p><strong>Correo:</strong> {{ psicologo.correo }}</p>

        <button @click="$router.back()">Volver</button>
    </div>
</div>

</template>

<script>
import axios from 'axios';

export default {
  name: 'PsicologoDetalle',

  data() {
    return {
      psicologo: null,
      loading: false,
      error: null
    };
  },

  methods: {
    async obtenerPsicologo() {
      const id = this.$route.params.id;

      console.log("ID recibido:", id);

      this.loading = true;
      try {
        const res = await axios.get(
          `http://127.0.0.1:8000/psicologos/${id}`
        );

        console.log("DETALLE:", res.data);

        this.psicologo = res.data;
      } catch (e) {
        this.error = e.message;
      } finally {
        this.loading = false;
      }
    }
  },

  mounted() {
    this.obtenerPsicologo();
  }
};
</script>

<style scoped>
.container {
  max-width: 600px;
  margin: auto;
}

.perfil {
  text-align: center;
}

img {
  width: 150px;
  border-radius: 50%;
}
</style>