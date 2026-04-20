<template>
<div class="card">
    <img :src="user.imagen" alt="Avatar">
    <h3>{{ user.nombre }}</h3>
    <p>📧 {{ user.descripcion }}</p>
    <p>📍 {{ user.ubicacion }}</p>
    <button class="btn-visitar" @click="$emit('ver', user.id)">Ver Psicólogo</button>
    <router-link :to="`/psicologos/${user.id}`">Ver Perfil</router-link>
  </div>

</template>

<script>
export default {
    name: 'UserComponent',
    props: {
        user: Object
    },
}
</script>

<style scoped>
.card {
  border: 1px solid #eee;
  border-radius: 12px;
  padding: 1rem;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
img {
    width: 80px;
    height: 80px;
}
.btn-visitar { 
    background: #42b883;
    color: white;
    border: none;
    padding: 5px 10px;
    border-radius: 4px;
}
</style>