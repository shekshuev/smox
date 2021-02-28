<template>
    <v-app>
        <v-navigation-drawer app clipped v-model="drawer">
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
        </v-navigation-drawer>
        <v-app-bar app clipped-left>
            <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
            <v-toolbar-title>Social Media Opinion Extractor | {{ title }}</v-toolbar-title>
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