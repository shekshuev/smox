<template>
    <v-container>
        <v-card class="mb-3">
            <v-list subheader rounded>
                <v-subheader>Профили доступа</v-subheader>
                <v-list-item v-for="profile in accessProfiles" v-bind:key="profile.id">
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
                <v-list-item link v-on:click="accessProfileDialog = true">
                    <v-list-item-content class="list-item-content-center">
                        <v-list-item-title class="primary--text">Добавить профиль</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-card>
        <v-card class="mb-3">
            <v-list subheader rounded>
                <v-subheader>Источники</v-subheader>
                <v-list-item v-for="source in sources" v-bind:key="source.id">
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
                <v-list-item link v-on:click="sourceDialog = true">
                    <v-list-item-content class="list-item-content-center">
                        <v-list-item-title class="primary--text">Добавить источник</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-card>
        <v-card class="mb-3">
            <v-list subheader rounded>
                <v-subheader>Настройка подключения к БД</v-subheader>
                <v-list-group>
                    <template v-slot:activator>
                        <v-list-item-title>MySQL</v-list-item-title>
                    </template>
                    <v-form ref="settings">
                        <v-list-item>
                            <v-list-item-content>
                                <v-row>
                                    <v-col cols="12" sm="3">
                                        <v-text-field label="Хост" v-model="dbHost"></v-text-field>
                                    </v-col>
                                    <v-col cols="12" sm="3">
                                        <v-text-field label="Имя базы данных" v-model="dbName"></v-text-field>
                                    </v-col>
                                    <v-col cols="12" sm="3">
                                        <v-text-field label="Логин" v-model="dbLogin"></v-text-field>
                                    </v-col>
                                    <v-col cols="12" sm="3">
                                        <v-text-field
                                            label="Пароль"
                                            v-model="dbPassword"
                                            :type="showPassword ? 'text' : 'password'"
                                            :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                                            @click:append="showPassword = !showPassword"
                                        ></v-text-field>
                                    </v-col>
                                </v-row>
                            </v-list-item-content>
                        </v-list-item>
                    </v-form>
                    <v-list-item link v-on:click="updateDbConnection">
                        <v-list-item-content class="list-item-content-center">
                            <v-list-item-title class="primary--text">Сохранить изменения</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </v-list-group>
            </v-list>
        </v-card>
        <v-card>
            <v-list subheader rounded>
                <v-subheader>Внешний вид</v-subheader>
                <v-list-item>
                    <v-list-item-content>
                        <v-list-item-title>Темная тема</v-list-item-title>
                    </v-list-item-content>
                    <v-list-item-action>
                        <v-switch v-model="dark_mode"></v-switch>
                    </v-list-item-action>
                </v-list-item>
            </v-list>
        </v-card>
        <v-dialog v-model="accessProfileDialog" max-width="600px" persistent>
            <v-card>
                <v-card-title>
                    <span class="headline">Новый профиль доступа</span>
                </v-card-title>
                <v-card-text>
                    <v-form ref="accessProfileForm">
                        <v-text-field v-model="name" v-bind:rules="rules" label="Название" required></v-text-field>
                        <v-text-field v-model="accessToken" v-bind:rules="rules" label="Токен" required></v-text-field>
                    </v-form>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" text v-on:click="addAccessProfile">Добавить</v-btn>
                    <v-btn color="primary" text v-on:click="accessProfileDialog = false">Отмена</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
        <v-dialog v-model="sourceDialog" max-width="600px" persistent>
            <v-card>
                <v-card-title>
                    <span class="headline">Новый источник</span>
                </v-card-title>
                <v-card-text>
                    <v-stepper v-model="step" vertical class="stepper">
                        <v-stepper-items>
                            <v-stepper-step step="0" :complete="step > 0">Профиль доступа</v-stepper-step>
                            <v-stepper-content step="0">
                                <v-select
                                    v-model="selectedAccessProfile"
                                    v-bind:items="accessProfiles"
                                    outlined
                                    dense
                                    label="Профиль доступа"
                                    item-text="name"
                                    return-object
                                ></v-select>
                                <v-btn v-if="selectedAccessProfile != null" color="primary" text v-on:click="step = 1"
                                    >Далее</v-btn
                                >
                            </v-stepper-content>
                            <v-stepper-step step="1" :complete="step > 1">Id или домен</v-stepper-step>
                            <v-stepper-content step="1">
                                <div class="stepper-content">
                                    <v-text-field v-model="request" label="Id или домен">
                                        <template v-slot:append>
                                            <v-progress-circular
                                                v-if="loading"
                                                indeterminate
                                                size="25"
                                            ></v-progress-circular>
                                        </template>
                                    </v-text-field>
                                    <v-list-item v-if="source != null">
                                        <v-list-item-avatar>
                                            <v-img :src="source.photo"></v-img>
                                        </v-list-item-avatar>
                                        <v-list-item-content>
                                            <v-list-item-title>{{ source.name }}</v-list-item-title>
                                            <v-list-item-subtitle>{{ source.description }}</v-list-item-subtitle>
                                        </v-list-item-content>
                                    </v-list-item>
                                    <v-btn color="primary" text v-on:click="step = 0">Назад</v-btn>
                                </div>
                            </v-stepper-content>
                        </v-stepper-items>
                    </v-stepper>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn v-if="source != null" color="primary" text v-on:click="saveSource">Добавить</v-btn>
                    <v-btn color="primary" text v-on:click="sourceDialog = false">Отмена</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
        <v-dialog v-model="confirmDialog" persistent max-width="290">
            <v-card>
                <v-card-title class="headline">Удалить объект?</v-card-title>
                <v-card-text v-if="deletableObject != null">
                    <v-list-item v-if="deletableObject.type == 'source'">
                        <v-list-item-avatar>
                            <v-img :src="deletableObject.payload.photo"></v-img>
                        </v-list-item-avatar>
                        <v-list-item-content>
                            <v-list-item-title>{{ deletableObject.payload.name }}</v-list-item-title>
                            <v-list-item-subtitle>{{ deletableObject.payload.description }}</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                    <v-list-item v-if="deletableObject.type == 'profile'">
                        <v-list-item-content>
                            <v-list-item-title>{{ deletableObject.payload.name }}</v-list-item-title>
                            <v-list-item-subtitle>{{ deletableObject.payload.access_token }}</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" text @click="() => closeConfirmDialog()">Отмена</v-btn>
                    <v-btn color="red" text @click="deleteObject">Да, удалить</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-container>
</template>
<script>
import Vue from "vue";
import { mapState } from "vuex";
import { addProfile, deleteProfile } from "src/api/access_profile";
import { ADD_ACCESS_PROFILE, DELETE_ACCESS_PROFILE } from "src/store/modules/access_profile/mutation_types";
import { createSource, searchSource, deleteSource } from "src/api/source";
import { ADD_SOURCE, DELETE_SOURCE } from "src/store/modules/source/mutation_types";
import { SET_APPEARANCE, UPDATE_DATABASE_CONNECTION } from "src/store/modules/settings/mutation_types";
import { updateDatatbaseConnection } from "src/api/settings";

export default Vue.component("settings", {
    title: "SMOX | Settings",
    data: function() {
        return {
            accessProfileDialog: false,
            sourceDialog: false,
            step: 0,
            source: null,
            selectedAccessProfile: null,
            request: "",
            loading: false,
            delay: 0,
            valid: false,
            name: "",
            rules: [(v) => !!v || "Поле обязательно для заполнения"],
            accessToken: "",
            confirmDialog: false,
            deletableObject: null,
            showPassword: false,
        };
    },
    computed: {
        ...mapState({
            sources: (state) => state.source.sources,
            accessProfiles: (state) => state.accessProfile.accessProfiles,
            db: (state) => state.settings.db,
        }),
        dark_mode: {
            get() {
                return this.$store.state.settings.appearance.dark_mode;
            },
            set() {
                this.$vuetify.theme.dark = !this.dark_mode;
                let appearance = Object.assign({}, this.$store.state.settings.appearance);
                appearance.dark_mode = !this.dark_mode;
                this.$store.dispatch(SET_APPEARANCE, appearance);
            },
        },
        dbHost: {
            get() {
                return this.$store.state.settings.db.host;
            },
            set(newVal) {
                let db = Object.assign({}, this.$store.state.settings.db);
                db.host = newVal;
                this.$store.dispatch(UPDATE_DATABASE_CONNECTION, db);
            },
        },
        dbName: {
            get() {
                return this.$store.state.settings.db.name;
            },
            set(newVal) {
                let db = Object.assign({}, this.$store.state.settings.db);
                db.name = newVal;
                this.$store.dispatch(UPDATE_DATABASE_CONNECTION, db);
            },
        },
        dbLogin: {
            get() {
                return this.$store.state.settings.db.login;
            },
            set(newVal) {
                let db = Object.assign({}, this.$store.state.settings.db);
                db.login = newVal;
                this.$store.dispatch(UPDATE_DATABASE_CONNECTION, db);
            },
        },
        dbPassword: {
            get() {
                return this.$store.state.settings.db.password;
            },
            set(newVal) {
                let db = Object.assign({}, this.$store.state.settings.db);
                db.password = newVal;
                this.$store.dispatch(UPDATE_DATABASE_CONNECTION, db);
            },
        },
    },
    watch: {
        request: async function(newRequest) {
            clearTimeout(this.delay);
            if (newRequest == "") return;
            this.delay = setTimeout(async () => {
                this.loading = true;
                this.source = await searchSource(newRequest, this.selectedAccessProfile.access_token);
                this.loading = false;
            }, 2000);
        },
    },
    methods: {
        async addAccessProfile() {
            if (this.$refs.accessProfileForm.validate()) {
                let result = await addProfile({ name: this.name, accessToken: this.accessToken });
                if (result != null) {
                    this.$store.dispatch(ADD_ACCESS_PROFILE, result);
                    this.name = "";
                    this.accessToken = "";
                    this.accessProfileDialog = false;
                    this.$refs.accessProfileForm.reset();
                }
            }
        },
        async deleteAccessProfile(profile) {
            this.deletableObject = {
                type: "profile",
                payload: profile,
            };
            this.confirmDialog = true;
        },
        async deleteSource(source) {
            this.deletableObject = {
                type: "source",
                payload: source,
            };
            this.confirmDialog = true;
        },
        async saveSource() {
            let result = await createSource(this.source);
            if (result != null) {
                this.$store.dispatch(ADD_SOURCE, result);
                this.sourceDialog = false;
                this.clearSource();
            }
        },
        clearSource() {
            this.source = null;
            this.request = "";
            this.loading = false;
            clearTimeout(this.delay);
            this.delay = 0;
        },
        async deleteObject() {
            if (this.deletableObject.type == "source") {
                if (await deleteSource(this.deletableObject.payload)) {
                    this.$store.dispatch(DELETE_SOURCE, this.deletableObject.payload);
                    this.closeConfirmDialog();
                }
            } else {
                if (await deleteProfile(this.deletableObject.payload)) {
                    this.$store.dispatch(DELETE_ACCESS_PROFILE, this.deletableObject.payload);
                    this.closeConfirmDialog();
                }
            }
        },
        closeConfirmDialog() {
            this.deletableObject = null;
            this.confirmDialog = false;
        },
        async updateDbConnection() {
            if (await updateDatatbaseConnection(this.db)) {
                console.log("fuck yeah!");
            }
        },
    },
});
</script>
<style>
.list-item-content-center {
    align-items: center;
    text-align: center !important;
}
.stepper {
    box-shadow: none;
}
.stepper-content {
    overflow-y: scroll;
    height: 100%;
}
</style>
