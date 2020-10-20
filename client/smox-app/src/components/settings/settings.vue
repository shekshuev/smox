<template>
    <v-container fluid>
        <v-row>
            <v-col>
                <v-simple-table>
                    <thead>
                        <tr>
                            <th>Номер</th>
                            <th>Название</th>
                            <th>Токен</th>
                            <th>Текущий</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(profile, index) in accessProfiles" v-bind:key="index">
                            <td>{{ index + 1 }}</td>
                            <td>{{ profile.name }}</td>
                            <td>{{ profile.accessToken }}</td>
                            <td>{{ profile.current }}</td>
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
    </v-container>
</template>
<script src="./settings.js"></script>