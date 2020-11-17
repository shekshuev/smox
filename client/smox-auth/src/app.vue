<template>
    <v-app>
        <v-main>
            <v-container class="fill-height" fluid>
                <v-row align="center" justify="center">
                    <v-col cols="12" sm="8" md="4">
                        <v-card class="elevation-12">
                            <v-toolbar flat>
                                <v-toolbar-title>{{ login ? "Вход" : "Регистрация" }}</v-toolbar-title>
                                <v-spacer></v-spacer>
                                <v-btn text large v-on:click="chooseRegisterOrLogin">
                                    <v-icon v-if="login" class="mr-1">mdi-account-plus</v-icon>
                                    <v-icon v-if="!login" class="mr-1">mdi-login</v-icon>
                                    {{ login ? "Регистрация" : " Вход" }}
                                </v-btn>
                            </v-toolbar>
                            <registerComponent v-if="!login" />
                            <loginComponent v-if="login" />
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>
        </v-main>
    </v-app>
</template>
<script src="./app.js"></script>