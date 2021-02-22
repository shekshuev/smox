import Vue from "vue";
import VueRouter from "vue-router";
import App from "./app.vue";
import vuetify from "./plugins/vuetify";

import store from "./store";

import DashboardComponent from "src/components/dashboard/dashboard.vue";
import SourceComponent from "src/components/source/source.vue";
import SettingsComponent from "src/components/settings/settings.vue";
import TaskComponent from "src/components/task/task.vue";
import PostComponent from "src/components/post/post.vue";
import NotFoundComponent from "src/components/notfound/notfound.vue";
import LogComponent from "src/components/logs/log.vue";
import AnalyticsComponent from "src/components/analytics/analytics.vue";

const router = new VueRouter({
    mode: "history",
    routes: [
        { path: "/", component: DashboardComponent },
        { path: "/sources", component: SourceComponent },
        { path: "/settings", component: SettingsComponent },
        { path: "/tasks", component: TaskComponent },
        { path: "/posts", component: PostComponent },
        { path: "/logs", component: LogComponent },
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
    render: h => h(App),
    components: {
        App 
    },
    beforeCreate() {
		this.$store.commit('initialiseStore');
	}
})
