import Vue from "vue";
import VueRouter from "vue-router";
import mainComponent from "./main.vue";
import "vuetify/dist/vuetify.min.css"

import vuetify from "./plugins/vuetify";

import DashboardComponent from "application/components/dashboard/dashboard.vue";
import SourceComponent from "application/components/source/source.vue";
import SettingsComponent from "application/components/settings/settings.vue";
import TaskComponent from "application/components/task/task.vue";
import PostComponent from "application/components/post/post.vue";
import NotFoundComponent from "application/components/notfound/notfound.vue";
import LogComponent from "application/components/logs/log.vue";


import store from "./store";



const router = new VueRouter({
    mode: "history",
    routes: [
        { path: "/", component: DashboardComponent },
        { path: "/sources", component: SourceComponent },
        { path: "/settings", component: SettingsComponent },
        { path: "/tasks", component: TaskComponent },
        { path: "/posts", component: PostComponent },
        { path: "/logs", component: LogComponent },
        { path: "*", component: NotFoundComponent }
    ]
});

Vue.use(VueRouter);

new Vue({
    el: "#app",
    template: "<mainComponent/>",
    components: {
        mainComponent
    },
    store,
    vuetify,
    router,
    beforeCreate() {
		this.$store.commit('initialiseStore');
	}
});