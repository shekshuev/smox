<template>
    <v-app>
        <v-app-bar app elevate-on-scroll>
            <v-app-bar-nav-icon @click="drawer = !drawer" />
            <v-toolbar-title>Social Media Opinion Extractor | {{ title }}</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-img class="mx-2" :src="logo" max-height="40" max-width="40" contain></v-img>
        </v-app-bar>
        <v-navigation-drawer fixed temporary v-model="drawer">
            <template v-slot:prepend>
                <v-list-item two-line>
                    <v-list-item-avatar>
                        <img :src="photo" />
                    </v-list-item-avatar>

                    <v-list-item-content>
                        <v-list-item-title>{{ username }}</v-list-item-title>
                        <v-list-item-subtitle>{{ role }}</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>
            </template>
            <v-divider></v-divider>
            <v-list dense>
                <v-list-item v-for="(key, index) in Object.keys(menu)" v-bind:key="index" link v-bind:to="key">
                    <v-list-item-action>
                        <v-icon>{{ menu[key].icon }}</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>{{ menu[key].title }}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
            <template v-slot:append>
                <form action="/logout" class="pa-2">
                    <v-btn text block type="submit">Logout</v-btn>
                </form>
            </template>
        </v-navigation-drawer>
        <v-main>
            <router-view> </router-view>
        </v-main>
    </v-app>
</template>

<script>
import Vue from "vue";

const logo = require("src/assets/logo.svg");

export default Vue.component("app", {
    data: function() {
        return {
            progress: 0,
            drawer: null,
            menu: {
                "/": {
                    icon: "mdi-view-dashboard",
                    title: "Главная",
                },
                "/analytics": {
                    icon: "mdi-database",
                    title: "Аналитика",
                },
                "/posts": {
                    icon: "mdi-post",
                    title: "Публикации",
                },
                "/tasks": {
                    icon: "mdi-calendar-check",
                    title: "Задания",
                },
                "/settings": {
                    icon: "mdi-cog",
                    title: "Настройки",
                },
            },
            username: localStorage.getItem("username"),
            role: localStorage.getItem("role"),
            photo: localStorage.getItem("photo") == null ? logo : localStorage.getItem("photo"),
            logo: require("src/assets/logo.svg"),
        };
    },
    methods: {
        logout() {
            //window.location = "/account/logout";
            console.log("logout");
        },
    },
    computed: {
        title: function() {
            return this.menu[this.$route.path].title;
        },
    },
});
</script>
