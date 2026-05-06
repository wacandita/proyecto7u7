<template>
  <div class="page-bg">
    <div class="container">

      <div v-if="loading" class="state-msg">Cargando perfil...</div>
      <div v-if="error" class="state-msg error">{{ error }}</div>

      <div v-if="psicologo" class="profile-card">

        <!-- Header con foto y nombre -->
        <div class="profile-header">
          <div class="avatar-ring">
            <img :src="psicologo.imagen" :alt="psicologo.nombre" />
          </div>
          <h1>{{ psicologo.nombre }}</h1>
          <span class="badge">Especialista en Salud Mental</span>
        </div>

        <!-- Cuerpo con info -->
        <div class="profile-body">
          <div class="info-row">
            <div class="info-icon">📝</div>
            <div>
              <span class="info-label">Descripción</span>
              <p class="info-value">{{ psicologo.descripcion }}</p>
            </div>
          </div>

          <div class="info-row">
            <div class="info-icon">📍</div>
            <div>
              <span class="info-label">Ubicación</span>
              <p class="info-value">{{ psicologo.ubicacion }}</p>
            </div>
          </div>

          <div class="info-row">
            <div class="info-icon">✉️</div>
            <div>
              <span class="info-label">Correo</span>
              <a :href="'mailto:' + psicologo.correo" class="info-value link">
                {{ psicologo.correo }}
              </a>
            </div>
          </div>
        </div>

        <!-- Botones -->
        <div class="profile-actions">
          <button class="btn-back" @click="$router.back()">← Volver</button>
          <button class="btn-primary">Agendar Cita</button>
        </div>

      </div>
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
      this.loading = true;
      try {
        const id = this.$route.params.id;
        const res = await axios.get(`http://127.0.0.1:8000/psicologos/${id}`);
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
.page-bg {
  min-height: 100vh;
  background: linear-gradient(135deg, #e8f4fd 0%, #f4f8ff 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
}

.container {
  width: 100%;
  max-width: 520px;
}

/* Card principal */
.profile-card {
  background: white;
  border-radius: 24px;
  box-shadow: 0 20px 60px rgba(52, 152, 219, 0.15);
  overflow: hidden;
}

/* Header azul degradado */
.profile-header {
  background: linear-gradient(135deg, #3498db, #2471a3);
  padding: 2.5rem 2rem 2rem;
  text-align: center;
  color: white;
}

.avatar-ring {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  border: 4px solid rgba(255,255,255,0.8);
  overflow: hidden;
  margin: 0 auto 1rem;
  box-shadow: 0 8px 25px rgba(0,0,0,0.2);
}

.avatar-ring img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.profile-header h1 {
  font-size: 1.6rem;
  font-weight: 800;
  margin: 0 0 0.5rem;
}

.badge {
  display: inline-block;
  background: rgba(255,255,255,0.2);
  color: white;
  padding: 0.3rem 1rem;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 600;
  backdrop-filter: blur(4px);
}

/* Cuerpo info */
.profile-body {
  padding: 1.8rem 2rem;
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
}

.info-row {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  padding: 1rem;
  background: #f8fbff;
  border-radius: 12px;
  border-left: 4px solid #3498db;
}

.info-icon {
  font-size: 1.3rem;
  margin-top: 2px;
}

.info-label {
  font-size: 0.75rem;
  font-weight: 700;
  color: #3498db;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  display: block;
  margin-bottom: 2px;
}

.info-value {
  font-size: 0.95rem;
  color: #2c3e50;
  margin: 0;
}

.link {
  color: #2980b9;
  text-decoration: none;
}

.link:hover {
  text-decoration: underline;
}

/* Botones */
.profile-actions {
  padding: 0 2rem 2rem;
  display: flex;
  gap: 1rem;
}

.btn-back {
  flex: 1;
  padding: 0.75rem;
  border: 2px solid #bdc3c7;
  background: transparent;
  color: #5d6d7e;
  border-radius: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-back:hover {
  border-color: #3498db;
  color: #3498db;
}

.btn-primary {
  flex: 2;
  padding: 0.75rem;
  background: linear-gradient(135deg, #3498db, #2471a3);
  color: white;
  border: none;
  border-radius: 12px;
  font-weight: 700;
  cursor: pointer;
  transition: opacity 0.2s ease;
  font-size: 0.95rem;
}

.btn-primary:hover {
  opacity: 0.88;
}

/* Estados */
.state-msg {
  text-align: center;
  padding: 1rem;
  color: #5d6d7e;
  font-weight: 500;
}

.state-msg.error {
  color: #e74c3c;
  background: #fdedec;
  border-radius: 8px;
}
</style>