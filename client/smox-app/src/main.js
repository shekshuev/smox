import Vue from "vue";
import VueRouter from "vue-router";
import Initial from "src/initial.vue";
import vuetify from "./plugins/vuetify";
import axios from "axios";

import store from "./store";

import DashboardComponent from "src/components/dashboard.vue";
import SettingsComponent from "src/components/settings.vue";
import TaskComponent from "src/components/task.vue";
import PostComponent from "src/components/post.vue";
import NotFoundComponent from "src/components/notfound.vue";
import AnalyticsComponent from "src/components/analytics.vue";

import titleMixin from "src/mixins/title.js";

axios.interceptors.request.use(
    function(config) {
        config.withCredentials = true;
        return config;
    },
    function(error) {
        if (error.response.status == 401) {
            localStorage.removeItem("accessToken");
            localStorage.removeItem("username");
            window.location.href = "/login";
        }
    }
);

axios.defaults.withCredentials = true;

const router = new VueRouter({
    mode: "history",
    routes: [
        { path: "/", component: DashboardComponent },
        { path: "/settings", component: SettingsComponent },
        { path: "/tasks", component: TaskComponent },
        { path: "/posts", component: PostComponent },
        { path: "/analytics", component: AnalyticsComponent },
        { path: "*", component: NotFoundComponent },
    ],
});

Vue.config.productionTip = false;
Vue.use(VueRouter);
Vue.mixin(titleMixin);

new Vue({
    title: "SMOX",
    el: "#app",
    vuetify,
    store,
    router,
    render: (h) => h(Initial),
    components: {
        Initial,
    },
    beforeCreate() {
        this.$store.commit("initialiseStore");
    },
});
