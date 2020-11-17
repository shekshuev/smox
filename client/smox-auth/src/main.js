import Vue from "vue";
import vuetify from "./plugins/vuetify";
import App from "./app.vue";

new Vue({
    el: "#app",
    vuetify,
    render: h => h(App),
    components: {
        App 
    }
})