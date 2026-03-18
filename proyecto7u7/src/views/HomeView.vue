<template>
  <div class="app-layout">
    <aside class="reddit-sidebar-left">
      <div class="sidebar-header">
        <div class="logo-wrapper">
          <img src="@/assets/mentesana-logo.png" alt="MenteSana Logo" class="logo-image">
        </div>
        <span class="logo-text">MenteSana</span>
      </div>

      <nav class="sidebar-nav">
        <div class="nav-section">
          <p class="section-label">FEEDS</p>
          <button @click="seccionActual = 'populares'" :class="{ active: seccionActual === 'populares' }" class="nav-item">
            <span class="icon">🔥</span> Popular
          </button>
          <button @click="seccionActual = 'reciente'" :class="{ active: seccionActual === 'reciente' }" class="nav-item">
            <span class="icon">✨</span> Reciente
          </button>
        </div>

        <div class="nav-section">
          <p class="section-label">TEMAS DE AYUDA</p>
          <button @click="seccionActual = 'ansiedad'" :class="{ active: seccionActual === 'ansiedad' }" class="nav-item">
            <span class="icon">🧘</span> Ansiedad
          </button>
          <button @click="seccionActual = 'noticias'" :class="{ active: seccionActual === 'noticias' }" class="nav-item">
            <span class="icon">📰</span> Noticias Salud
          </button>
          <button @click="seccionActual = 'duelo'" :class="{ active: seccionActual === 'duelo' }" class="nav-item">
            <span class="icon">🤍</span> Duelo y Pérdida
          </button>
          <button @click="seccionActual = 'autoestima'" :class="{ active: seccionActual === 'autoestima' }" class="nav-item">
            <span class="icon">⭐</span> Autoestima
          </button>
        </div>

        <div class="nav-section">
          <p class="section-label">RECURSOS</p>
          <button @click="seccionActual = 'recursos'" :class="{ active: seccionActual === 'recursos' }" class="nav-item">
            <span class="icon">📚</span> Guías PDF
          </button>
          <button @click="seccionActual = 'lineas'" :class="{ active: seccionActual === 'lineas' }" class="nav-item">
            <span class="icon">📞</span> Líneas de Crisis
          </button>
        </div>

        <div class="nav-section">
          <p class="section-label">USUARIO</p>
          <router-link to="/registro" class="nav-item"><span class="icon">⚙️</span> Ajustes</router-link>
          <button class="nav-item"><span class="icon">🌙</span> Modo Oscuro</button>
        </div>
      </nav>
    </aside>

    <div class="right-side-wrapper">
      
      <header class="top-nav">
        <div class="search-container">
          <input type="text" placeholder="Buscar en la comunidad..." class="reddit-search">
        </div>
        <div class="user-pill">Anónimo 🔒</div>
      </header>

      <main class="main-content">
        <div class="content-grid">
          
          <section class="posts-column">
            <h2 class="page-title">{{ seccionActual.toUpperCase() }}</h2>
            
            <div v-if="seccionActual === 'populares'">
              <div v-for="i in 3" :key="'pop-'+i" class="reddit-card">
                <div class="votes">▲ <br> 85 <br> ▼</div>
                <div class="card-info">
                  <span class="community-tag">r/salud_mental</span>
                  <h3>Post Popular #{{i}}</h3>
                  <p>¿Cómo se sienten hoy? Espacio de desahogo libre...</p>
                  <div class="card-footer">💬 24 Comentarios | ⤴ Compartir</div>
                </div>
              </div>
            </div>

            <div v-else-if="seccionActual === 'reciente'">
              <div class="reddit-card">
                <div class="votes">▲ <br> 2 <br> ▼</div>
                <div class="card-info">
                  <span class="community-tag">r/nuevo</span>
                  <h3>Contenido recién publicado</h3>
                  <p>Alguien acaba de compartir su historia...</p>
                  <div class="card-footer">💬 0 Comentarios | ⤴ Compartir</div>
                </div>
              </div>
            </div>

            <div v-else-if="seccionActual === 'ansiedad'">
              <div class="reddit-card">
                <div class="card-info">
                  <h3>Técnicas de Control de Ansiedad</h3>
                  <p>Información y ejercicios para momentos difíciles.</p>
                </div>
              </div>
            </div>

            <div v-else-if="seccionActual === 'recursos'">
              <div class="reddit-card">
                <div class="card-info">
                  <h3>Biblioteca de Guías PDF</h3>
                  <p>Material descargable para tu bienestar.</p>
                </div>
              </div>
            </div>

            <div v-else>
              <div class="reddit-card">
                <div class="card-info">
                  <h3>Sección {{ seccionActual }}</h3>
                  <EspacioComentario></EspacioComentario>
                </div>
              </div>
            </div>
          </section>

          <aside class="reddit-sidebar-right">
            <div class="right-card about-card">
              <div class="card-banner"></div>
              <div class="card-title">Sobre MenteSana</div>
              <div class="card-desc">
                Comunidad de apoyo mutuo. Somos un espacio seguro para compartir tus emociones de forma anónima.
              </div>
              <button class="btn-primary">Unirse a la Comunidad</button>
            </div>

            <div class="right-card help-resources">
              <div class="card-header-simple">RECURSOS DE AYUDA 🆘</div>
              <ul class="help-list">
                <li>
                  <a href="https://www.asivamosensalud.org" target="_blank">Línea Nacional de Apoyo</a>
                  <span>Atención 24/7 gratuita</span>
                </li>
                <li>
                  <a href="#">Chat con Psicólogo</a>
                  <span>Ayuda inmediata</span>
                </li>
              </ul>
            </div>

            <div class="right-card rules-card">
              <div class="card-header-simple">NORMAS</div>
              <ol class="rules-list">
                <li>No juzgar a los demás.</li>
                <li>Respetar el anonimato.</li>
                <li>Ser empático y amable.</li>
              </ol>
            </div>
          </aside>

        </div>
      </main>
    </div>
  </div>
</template>

<script>
import EspacioComentario from '@/components/CrearComentario.vue'

export default {
  
  data() {
    return {
      seccionActual: 'populares'
    }
  },
  components: {
    EspacioComentario,

  }
}
</script>

<style scoped>
/* Layout Principal */
.app-layout {
  display: flex;
  min-height: 100vh;
  background-color: #E6E9EE;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* BARRA IZQUIERDA */
.reddit-sidebar-left {
  width: 280px;
  background: white;
  border-right: 1px solid #C4CBD3;
  position: sticky;
  top: 0;
  height: 100vh;
  display: flex;
  flex-direction: column;
  text-align: left;
}

.sidebar-header {
  padding: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  border-bottom: 1px solid #E6E9EE;
  background: #fff;
  min-height: 220px;
}

.logo-wrapper {
  width: 100%;
  height: 160px;
  overflow: hidden;
  background: #fcfcfc;
}

.logo-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.logo-text {
  padding: 10px 0;
  font-weight: 800;
  font-size: 24px;
  color: #2c3e50;
  text-transform: uppercase;
  letter-spacing: -1.5px;
}

/* Menú Navegación */
.sidebar-nav { overflow-y: auto; flex: 1; padding: 10px 0; }
.nav-section { margin-bottom: 15px; padding: 0 12px; }
.section-label { font-size: 11px; font-weight: 700; color: #5f6c7a; margin-bottom: 5px; padding-left: 12px; }

.nav-item {
  display: flex; align-items: center; width: 100%; padding: 10px 12px;
  border: none; background: none; cursor: pointer; border-radius: 4px;
  font-size: 14px; color: #34495e; transition: 0.2s;
  text-decoration: none;
}
.nav-item:hover { background: #F0F2F5; }
.nav-item.active { background: #EAF0F6; font-weight: 700; border-right: 4px solid #4B8DCB; color: #4B8DCB; }
.icon { margin-right: 12px; font-size: 18px; }

/* WRAPPER DERECHO */
.right-side-wrapper { flex: 1; display: flex; flex-direction: column; }

.top-nav {
  height: 55px; background: white; border-bottom: 1px solid #C4CBD3;
  display: flex; align-items: center; padding: 0 20px; justify-content: space-between;
}
.reddit-search { width: 500px; background: #F0F2F5; border: 1px solid #C4CBD3; padding: 8px 15px; border-radius: 20px; }
.user-pill { font-weight: bold; font-size: 14px; background: #F0F2F5; padding: 5px 15px; border-radius: 20px; color: #34495e; }

/* GRID DE CONTENIDO */
.main-content { padding: 20px; }
.content-grid { display: flex; justify-content: center; gap: 24px; max-width: 1200px; margin: 0 auto; }

.posts-column { flex: 1; max-width: 640px; }
.page-title { text-align: left; font-size: 14px; font-weight: bold; margin-bottom: 15px; color: #2c3e50; }

/* Cards */
.reddit-card { background: white; border: 1px solid #C4CBD3; border-radius: 4px; display: flex; margin-bottom: 10px; text-align: left; }
.votes { background: #F8F9FB; padding: 10px; width: 40px; font-weight: bold; color: #34495e; font-size: 12px; }
.card-info { padding: 10px; flex: 1; }
.community-tag { font-size: 12px; font-weight: bold; color: #2c3e50; }
.card-info h3 { margin: 5px 0; font-size: 18px; color: #2c3e50; }
.card-footer { font-size: 12px; color: #5f6c7a; margin-top: 10px; font-weight: bold; }

/* Sidebar Derecha */
.reddit-sidebar-right { width: 312px; display: flex; flex-direction: column; gap: 15px; }
.right-card { background: white; border: 1px solid #C4CBD3; border-radius: 4px; text-align: left; overflow: hidden; }
.card-banner { height: 34px; background: #4B8DCB; }
.card-title { padding: 12px; font-weight: bold; color: #2c3e50; }
.card-desc { padding: 0 12px 12px; font-size: 14px; color: #34495e; }
.btn-primary { width: calc(100% - 24px); margin: 12px; background: #4B8DCB; color: white; border: none; padding: 10px; border-radius: 20px; font-weight: bold; cursor: pointer; }

.card-header-simple { background: #F8F9FB; padding: 12px; font-size: 11px; font-weight: bold; color: #5f6c7a; }
.help-list { list-style: none; padding: 12px; margin: 0; }
.help-list a { color: #0079d3; font-weight: bold; text-decoration: none; font-size: 14px; }
.help-list span { display: block; font-size: 12px; color: #5f6c7a; }
.rules-list { padding: 12px 12px 12px 30px; font-size: 13px; margin: 0; color: #34495e; }
</style>