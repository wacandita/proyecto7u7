<template>
  <div>
    <p v-if="loading">Cargando...</p>
    <p v-if="error">{{ error }}</p>

    <div class="grid">
      <CardComponent 
        :users="users"
      />
    </div>
  </div>
</template>


<script>
import axios from 'axios';
import CardComponent from '../components/CardComponent.vue';

export default {
  name: 'PsicologosView',

  components: {
    CardComponent
  },

  data() {
    return {
      users: [],
      loading: false,
      error: null
    };
  },

  methods: {
    async obtenerPsicologos() {
      this.loading = true;
      try {
        const response = await axios.get('http://127.0.0.1:8000/psicologos');
        this.users = response.data;
      } catch (error) {
        this.error = error.message;
      } finally {
        this.loading = false;
      }
    }
  },

  mounted() {
    this.obtenerPsicologos();
  }
};
</script>

<style scoped>
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 1rem;
}
</style>