<template>
    <v-container>
        <v-card class="mb-3">
            <v-list subheader rounded>
                <v-subheader>Профили доступа</v-subheader>
                <v-list-item v-for="profile in accessProfiles" v-bind:key="profile.id" >
                    <v-list-item-content>
                        <v-list-item-title>{{ profile.name }}</v-list-item-title>
                        <v-list-item-subtitle>{{ profile.access_token }}</v-list-item-subtitle>
                    </v-list-item-content>
                    <v-list-item-action>
                        <v-btn icon v-on:click="deleteAccessProfile(profile)">
                            <v-icon>mdi-delete</v-icon>
                        </v-btn>
                    </v-list-item-action>
                </v-list-item>
                <v-list-item link>
                    <v-list-item-content class="list-item-content-center">
                        <v-list-item-title  class="primary--text">Добавить профиль</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-card>
        <v-card class="mb-3">
            <v-list subheader rounded>
                <v-subheader>Источники</v-subheader>
                <v-list-item v-for="source in sources" v-bind:key="source.id" >
                    <v-list-item-avatar>
                        <v-img :src="source.photo"></v-img>
                    </v-list-item-avatar>
                    <v-list-item-content>
                        <v-list-item-title>{{ source.name }}</v-list-item-title>
                        <v-list-item-subtitle>{{ source.description }}</v-list-item-subtitle>
                    </v-list-item-content>
                    <v-list-item-action>
                        <v-btn icon v-on:click="deleteSource(source)">
                            <v-icon>mdi-delete</v-icon>
                        </v-btn>
                    </v-list-item-action>
                </v-list-item>
                <v-list-item link>
                    <v-list-item-content class="list-item-content-center">
                        <v-list-item-title class="primary--text">Добавить источник</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-card>
        <v-card>
            <v-list subheader rounded>
                <v-subheader>Внешний вид</v-subheader>
                <v-list-item >
                    <v-list-item-content>
                        <v-list-item-title>Темная тема</v-list-item-title>
                    </v-list-item-content>
                    <v-list-item-action>
                        <v-switch v-model="dark_mode"></v-switch>
                    </v-list-item-action>
                </v-list-item>
            </v-list>
        </v-card>
    </v-container>
    <!--<v-container fluid>
        <v-row>
            <v-col>
                <v-simple-table>
                    <thead>
                        <tr>
                            <th>Номер</th>
                            <th>Название</th>
                            <th>Токен</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(profile, index) in accessProfiles" v-bind:key="index">
                            <td>{{ index + 1 }}</td>
                            <td>{{ profile.name }}</td>
                            <td>{{ profile.access_token }}</td>
                            <td>
                                <v-btn icon>
                                    <v-icon v-on:click="deleteAccessProfile(profile)">mdi-delete</v-icon>
                                </v-btn>
                            </td>
                        </tr>
                    </tbody>
                </v-simple-table>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-form v-model="valid">
                    <v-container>
                        <v-row>
                            <v-col md="4">
                                <v-text-field v-model="name" v-bind:rules="rules" label="Название" required></v-text-field>
                            </v-col>
                            <v-col md="8">
                                <v-text-field v-model="accessToken" v-bind:rules="rules" label="Токен" required></v-text-field>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col class="d-flex flex-row-reverse">
                                <v-btn color="primary" v-on:click="addAccessProfile">Добавить</v-btn> 
                            </v-col>
                        </v-row>
                    </v-container>
                </v-form>
            </v-col>
        </v-row>
    </v-container>-->
</template>
<style>
    .list-item-content-center
    {
        align-items: center;
        text-align: center !important;
    }
</style>
<script src="./settings.js"></script>