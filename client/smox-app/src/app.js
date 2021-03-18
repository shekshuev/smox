import Vue from "vue";

const logo = require("src/assets/logo.svg");

export default Vue.component("app",
{
    data: function()
    {
        return {
            progress: 0,
            drawer: null,
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
                }
            },
            username: localStorage.getItem("username"),
            role: localStorage.getItem("role"),
            photo: localStorage.getItem("photo") == null ? logo : localStorage.getItem("photo"),
            logo: require("src/assets/logo.svg")
        }
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