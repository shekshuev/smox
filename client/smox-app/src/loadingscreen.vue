<template>
    <v-app>
        <v-container bg fill-height grid-list-md text-xs-center>
            <v-layout row wrap align-center>
                <v-flex>
                    <h1 class="display-4 text-center">SMOX</h1>
                    <v-progress-linear :value="progress" color="primary" height="15"></v-progress-linear>
                    <p class="text-center text--secondary subtitle-1">social media opinion extractor</p>
                </v-flex>
            </v-layout>
        </v-container>
    </v-app>
</template>
<script src="./loadingscreen.js"></script>