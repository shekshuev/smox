import Vue from "vue";
import vuetify from "./plugins/vuetify";
import App from "./app.vue";
import axios from "axios";

import titleMixin from "src/mixins/title.js";

axios.interceptors.response.use(null, error => 
{
    if (error.response.status == 401)
    {
        localStorage.removeItem("accessToken");
        localStorage.removeItem("username");
        window.location.href = "/login";
    }
    throw error;
});

Vue.mixin(titleMixin);

new Vue({
    el: "#app",
    vuetify,
    render: h => h(App),
    components: {
        App 
    }
})