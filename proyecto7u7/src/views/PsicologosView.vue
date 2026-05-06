<template>
  <div class="page-container">
    <p v-if="loading">Cargando...</p>
    <p v-if="error">{{ error }}</p>

    <div class="grid">
      <CardComponent :users="users" />
    </div>

    <div v-if="!loading && !error && psicologo" class="profile-card-detailed">
      <div class="profile-header">
        <div class="image-wrapper">
          <img :src="psicologo.foto" alt="Foto de Perfil" />
        </div>
        <h1>{{ psicologo.nombre }}</h1>
        <p class="title-specialty">Especialista en Salud Mental</p>
      </div>

      <div class="profile-body">
        <div class="info-group">
          <span class="icon">📝</span>
          <p><strong>Descripción:</strong> {{ psicologo.descripcion }}</p>
        </div>
        <div class="info-group">
          <span class="icon">📍</span>
          <p><strong>Ubicación:</strong> {{ psicologo.ubicacion }}</p>
        </div>
        <div class="info-group">
          <span class="icon">✉️</span>
          <p><strong>Correo:</strong> <a :href="'mailto:' + psicologo.correo">{{ psicologo.correo }}</a></p>
        </div>
      </div>

      <div class="profile-actions">
        <button class="btn-back" @click="$router.back()">Volver</button>
        <button class="btn-primary">Agendar Cita</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import CardComponent from '../components/CardComponent.vue';

export default {
  name: 'PsicologosView',
  components: { CardComponent },

  data() {
    return {
      users: [],
      psicologo: null,   // ← faltaba esto
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

<style scoped>

div {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  background-color: #f9fbff; 
  font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
}


.grid {
  display: grid;
  
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 2rem;
  padding: 1rem 0;
}


p {
  text-align: center;
  font-weight: 500;
  color: #5d6d7e;
  padding: 1rem;
}

p[v-if="error"] {
  color: #e74c3c;
  background: #fdedec;
  border-radius: 8px;
}


:deep(.card) {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  border: 1px solid #e1e8f0;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

:deep(.card:hover) {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}


:deep(.card img) {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 1rem;
  border: 3px solid #3498db;
}


:deep(.card button) {
  background-color: #3498db;
  color: white;
  border: none;
  padding: 0.6rem 1.2rem;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 600;
  margin-top: 1rem;
  width: 100%;
}

:deep(.card button:hover) {
  background-color: #2980b9;
}
</style>  

