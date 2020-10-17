<template>
    <div>
        <v-card-text>
            <v-alert type="error" dismissible transition="fade-transition" :value="error" >{{ errorMessage }}</v-alert>
        </v-card-text>
        <v-card-text>
            <v-text-field label="Имя пользователя" name="login" v-model="username" prepend-icon="person" type="text"></v-text-field>
            <v-text-field label="Пароль" name="password" v-model="password" prepend-icon="lock" type="password"></v-text-field>
        </v-card-text>
        <v-card-text class="d-flex flex-row-reverse">
            <v-btn color="primary" depressed :disabled="loading" :loading="loading" v-on:click="login">Войти</v-btn>
        </v-card-text>
    </div>
</template>
<script src="./login.js"></script>