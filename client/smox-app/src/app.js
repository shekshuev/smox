import Vue from "vue";

export default Vue.component("app",
{
    data: function()
    {
        return {
            progress: 0,
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
                }
            }
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