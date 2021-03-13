import Vue from "vue";
import VueRouter from "vue-router";
import Initial from "src/initial.vue";
import vuetify from "./plugins/vuetify";

import store from "./store";

import DashboardComponent from "src/components/dashboard/dashboard.vue";
import SettingsComponent from "src/components/settings/settings.vue";
import TaskComponent from "src/components/task/task.vue";
import PostComponent from "src/components/post/post.vue";
import NotFoundComponent from "src/components/notfound/notfound.vue";
import AnalyticsComponent from "src/components/analytics/analytics.vue";

const router = new VueRouter({
    mode: "history",
    routes: [
        { path: "/", component: DashboardComponent }, 
        { path: "/settings", component: SettingsComponent },
        { path: "/tasks", component: TaskComponent },
        { path: "/posts", component: PostComponent },
        { path: "/analytics", component: AnalyticsComponent },
        { path: "*", component: NotFoundComponent }
    ]
});

Vue.config.productionTip = false
Vue.use(VueRouter);

new Vue({
    el: "#app",
    vuetify,
    store,
    router,
    render: h => h(Initial),
    components: {
        Initial 
    },
    beforeCreate() {
		this.$store.commit('initialiseStore');
	}
})
