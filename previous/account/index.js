import Vue from "vue";
import vuetify from "./plugins/vuetify";
import mainComponent from "./main.vue";

new Vue({
    el: "#app",
    template: "<mainComponent/>",
    vuetify,
    components: {
        mainComponent
    }
});