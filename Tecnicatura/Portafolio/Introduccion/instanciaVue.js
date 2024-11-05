const mensajeAUsuario = {
    data() {
        return {
            mensaje: 'Hola Javascript con vue.js'
        }
    }
}
Vue.createApp(mensajeAUsuario).mount('#app')
