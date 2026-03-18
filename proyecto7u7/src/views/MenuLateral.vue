<template>
  <div class="menu-lateral">
    <h3>Explorar</h3>
    <nav>
      <button @click="$emit('cambiar-seccion', 'populares')" class="menu-item">
        <span class="icon">🔥</span> Populares
      </button>
      <button @click="$emit('cambiar-seccion', 'noticias')" class="menu-item">
        <span class="icon">📰</span> Noticias de Salud
      </button>
      <button @click="$emit('cambiar-seccion', 'recursos')" class="menu-item">
        <span class="icon">📚</span> Biblioteca de Apoyo
      </button>
      <button @click="$emit('cambiar-seccion', 'grupos')" class="menu-item">
        <span class="icon">👥</span> Grupos de Apoyo
      </button>
    </nav>
    <hr>
    <div class="user-status">
      <p>Modo: <strong>Anónimo</strong> 🔒</p>
    </div>
  </div>
</template>

<style scoped>
.menu-lateral {
  background: white;
  padding: 20px;
  border-radius: 5px;
  border: 1px solid #ccc;
  text-align: left;
}
h3 { color: #7c7c7c; font-size: 0.8em; text-transform: uppercase; margin-bottom: 15px; }
nav { display: flex; flex-direction: column; gap: 5px; }
.menu-item {
  background: none;
  border: none;
  padding: 10px;
  text-align: left;
  cursor: pointer;
  border-radius: 5px;
  font-size: 1em;
  transition: 0.2s;
}
.menu-item:hover { background-color: #f6f7f8; }
.icon { margin-right: 10px; }
hr { border: 0.5px solid #eee; margin: 20px 0; }
.user-status { font-size: 0.85em; color: #42b983; }
</style>