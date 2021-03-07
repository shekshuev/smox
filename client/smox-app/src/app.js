import Vue from "vue";
import { LOAD_ACCESS_PROFILES } from "./store/modules/access_profile/mutation_types";
import { READ_DATABASE_CONNECTION } from "./store/modules/settings/mutation_types";
import { LOAD_SOURCES } from "./store/modules/source/mutation_types";
import { LOAD_TASKS } from "./store/modules/task/mutation_types";
import { READ_TARGETS } from "./store/modules/target/mutation_types";

export default Vue.component("app",
{
    data: function()
    {
        return {
            drawer: false,
            menu: {
                "/": {
                    "icon": "mdi-view-dashboard",
                    "title": "Главная",
                },
                "/analytics": {
                    "icon": "mdi-database",
                    "title": "Аналитика",
                },
                "/posts": {
                    "icon": "mdi-post",
                    "title": "Публикации",
                },
                "/tasks": 
                {
                    "icon": "mdi-calendar-check",
                    "title": "Задания"
                },
                "/settings": {
                    "icon": "mdi-cog",
                    "title": "Настройки",
                },
                "/logs": {
                    "icon": "mdi-notebook",
                    "title": "Логи",
                }
            }
        }
    },
    created: function()
    {
        this.$vuetify.theme.dark = this.$store.state.settings.appearance.dark_mode
        this.$store.dispatch(LOAD_ACCESS_PROFILES);
        this.$store.dispatch(LOAD_SOURCES);
        this.$store.dispatch(LOAD_TASKS);
        this.$store.dispatch(READ_TARGETS);
        this.$store.dispatch(READ_DATABASE_CONNECTION);
    },
    methods: 
    {
        logout()
        {
            //window.location = "/account/logout";
            console.log("logout")
        }
    },
    computed: 
    {
        title: function()
        {
            return this.menu[this.$route.path].title;
        }
    }
})