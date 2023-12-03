<template>
    <v-app>
        <v-container fluid bg fill-height>
            <v-layout column align-center>
                <v-img :src="mainlogo" max-width="400" contain></v-img>
                <v-progress-linear :value="progress" color="primary" height="15"></v-progress-linear>
            </v-layout>
        </v-container>
    </v-app>
</template>
<script>
import Vue from "vue";

export default Vue.component("loadingscreen", {
    props: ["progress"],
    data: function() {
        return {
            mainlogo: require("src/assets/mainlogo.svg"),
        };
    },
});
</script>
