<template>
    <v-app>
        <v-container bg fill-height grid-list-md text-xs-center>
            <v-layout row wrap align-center>
                <v-flex>
                    <v-img :src="mainlogo"></v-img>
                    <v-progress-linear :value="progress" color="primary" height="15"></v-progress-linear>
                </v-flex>
            </v-layout>
        </v-container>
    </v-app>
</template>
<script src="./loadingscreen.js"></script>