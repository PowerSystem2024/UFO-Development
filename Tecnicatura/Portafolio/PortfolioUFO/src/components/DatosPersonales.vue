<script setup>
import linkedin from '/src/assets/linkedin_icon.svg';
import instagram from '/src/assets/instagram_icon.svg';
import github from '/src/assets/github_icon.svg';

const title = 'UFO-Development';
const descripcion = 'Grupo N° 14 de la Tecnicatura en Programacion - UTN';
const residencia = 'San Rafael, Mendoza, Argentina';
const presentacion = 'Hola, bienvenidos al portafolio de proyectos de UFO-Development. Somos un grupo de estudiantes de la tecnicatura en programación con experiencia en el desarrollo de software, aplicaciones web y móviles. Nos enfocamos en crear soluciones innovadoras y funcionales que cumplen con las necesidades tecnológicas actuales. ¡Exploren nuestros proyectos y conozcan más sobre nuestro trabajo!';
const redesSociales = [
  { id: 1, name: 'linkedin', src: linkedin, url: 'https://www.linkedin.com/' },
  { id: 2, name: 'Instagram', src: instagram, url: 'https://www.instagram.com/' },
  { id: 3, name: 'github', src: github, url: 'https://github.com/PowerSystem2024/UFO-Development' },
  
];
const mail = 'UFO-Development@gmail.com';
</script>

<template>
  <section class="datos-personales">
    <div class="card">
      <h1>{{ title }}</h1>
      <h2>{{ descripcion }}</h2>
      <p>{{ presentacion }}</p>
      <ul class="container-lista">
        <li v-for="red in redesSociales" :key="red.id">
          <a :href="red.url"><img class="icon-redsocial" :src="red.src" width="35rem" :alt="red.name"></a>
        </li>
      </ul>
      <h3>💻✉️ Mail de contacto: {{ mail }}</h3>
      <h4>{{ residencia }}</h4>
    </div>
  </section>
</template>

<style scoped>
h1 {
  font-size: 2.5rem;
}

p {
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.card {
  background: linear-gradient(to right, #330d53c8, #7a3b7f, #330d53c8);
  animation: gradient 15s ease infinite;
  border-radius: 10px;
  padding: 10px;
  margin: 10px;
  text-align: center;
}

.container-lista {
  display: flex;
  justify-content: center;
  list-style: none;
  padding: 0;
  margin: 0;
  text-align: center;
}

.icon-redsocial {
  align-items: center;
  background-color: aliceblue;
  border-radius: 50%;
  padding: 2px;
  margin: 5px;
  box-shadow: 0 0 5px rgba(95, 124, 205, 0.934);
}

.icon-redsocial:hover {
  background-color: rgb(28, 41, 52);
  box-shadow: 0 0 5px rgba(251, 249, 249, 0.934);
}

h3 {
  font-size: 1.2rem;
  font-weight: 600;
}
</style>