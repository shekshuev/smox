<template>
    <v-card outlined :loading="loading" :disabled="loading">
        <v-card-text class="text-center">
            <p class="display-1">SMOX</p>
            <p class=" title">Вход</p>
            <v-icon size="120">mdi-account-circle</v-icon>
            <v-text-field label="Имя пользователя" name="login" v-model="username" prepend-icon="mdi-account" type="text"></v-text-field>
            <v-text-field label="Пароль" name="password" v-model="password" prepend-icon="mdi-lock" type="password"></v-text-field>
        </v-card-text>
        <v-card-actions class="justify-center">
            <v-btn text color="primary"  :disabled="loading" v-on:click="login">Войти</v-btn>
        </v-card-actions>
    </v-card>
</template>
<script src="./login.js"></script>