<template>
    <v-app>
        <v-navigation-drawer app clipped v-model="drawer">
            <v-list dense>
                <v-list-item link to="/">
                    <v-list-item-action>
                        <v-icon>mdi-view-dashboard</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>Главная</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item link to="/sources">
                    <v-list-item-action>
                        <v-icon>mdi-database</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>Аналитика</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item link to="/posts">
                    <v-list-item-action>
                        <v-icon>mdi-post</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>Управление публикациями</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item link to="/settings">
                    <v-list-item-action>
                        <v-icon>mdi-cog</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>Настройки</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
        <v-app-bar app clipped-left>
            <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
            <v-toolbar-title>Application</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn icon v-on:click="logout">
                <v-icon>mdi-logout</v-icon>
            </v-btn>
        </v-app-bar>
        <v-main>
            <router-view> </router-view>
        </v-main>
    </v-app>
</template>
<script src="./app.js"></script>
<style>
</style>