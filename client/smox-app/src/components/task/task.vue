<template>
    <v-container>
        <v-card class="md-3">
            <v-list subheader rounded>
                <v-subheader>Задания</v-subheader>
                <v-list-group v-for="task in tasks" v-bind:key="task.id">
                    <template v-slot:activator>
                        <v-list-item-content>
                            <v-list-item-title>{{ task.title }}</v-list-item-title>
                            <v-list-item-subtitle v-if="!task.is_finished">Задание активно с {{ new Date(task.begin_datetime).toLocaleDateString() + " " + new Date(task.begin_datetime).toLocaleTimeString() }}</v-list-item-subtitle>
                            <v-list-item-subtitle v-if="task.is_finished">Задание завершено. 
                                {{  "Загружено " + 0 + " публикаций из " + task.task_sources.length + " источников" + 
                                    " с " + new Date(task.begin_datetime).toLocaleDateString() + " " + new Date(task.begin_datetime).toLocaleTimeString() +
                                    " по " + new Date(task.end_datetime).toLocaleDateString() + " " + new Date(task.end_datetime).toLocaleTimeString() }}
                            </v-list-item-subtitle>
                        </v-list-item-content>
                        <v-list-item-action>
                            <v-menu>
                                <template v-slot:activator="{ on, attrs }">
                                    <v-btn icon v-on="on" v-bind="attrs">
                                        <v-icon>mdi-dots-vertical</v-icon>
                                    </v-btn>
                                </template>
                                <v-list>
                                    <v-list-item link v-on:click="stopTask(task)" v-bind:disabled="task.is_finished">
                                        <v-list-item-icon>
                                            <v-icon>mdi-stop</v-icon>
                                        </v-list-item-icon>
                                        <v-list-item-title>Завершить задание</v-list-item-title>       
                                    </v-list-item>
                                    <v-list-item link v-on:click="deleteTask(task)" v-bind:disabled="!task.is_finished">
                                        <v-list-item-icon>
                                            <v-icon>mdi-delete</v-icon>
                                        </v-list-item-icon>
                                        <v-list-item-title>Удалить</v-list-item-title>
                                    </v-list-item>
                                </v-list>
                            </v-menu>
                        </v-list-item-action>
                    </template>
                    <v-list-item v-for="taskSource in task.task_sources" v-bind:key="taskSource.id">
                        <v-list-item-avatar>
                            <v-img :src="taskSource.source.photo"></v-img>
                        </v-list-item-avatar>
                        <v-list-item-content>
                            <v-list-item-title>{{ taskSource.source.name }}</v-list-item-title>
                            <v-list-item-subtitle>{{ taskSource.source.description }}</v-list-item-subtitle>
                            <v-list-item-subtitle>Загружено публикаций: {{ taskSource.total_objects_downloaded }}</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                </v-list-group>
            </v-list>
        </v-card>
        <v-btn v-on:click="dialog=true" color="primary" fab fixed bottom right>
            <v-icon>mdi-plus</v-icon>
        </v-btn>
        <v-dialog id="newTaskDialog" v-model="dialog" max-width="600px" persistent>
            <v-card>
                <v-card-title>
                    <span class="headline">Новый источник</span>
                </v-card-title>
                <v-card-text>
                    <v-select v-bind:rules="rules.accessProfile" required v-model="selectedAccessProfile" :items="accessProfiles" label="Профиль доступа">
                        <template v-slot:selection="{ item, on }">
                            <v-list-item v-on="on">{{ item.name }}</v-list-item>
                        </template>
                        <template v-slot:item="{ item, on }">
                            <v-list-item v-on="on">{{ item.name }}</v-list-item>
                        </template>
                    </v-select>
                    <v-select v-bind:rules="rules.sources" required v-model="selectedSources" :items="sources" return-object item-text="name" label="Источники" multiple chips>
                        <template v-slot:selection="{ item, index }">
                            <v-chip v-if="index === 0">
                                <span>{{ item.name }}</span>
                            </v-chip>
                            <span v-if="index === 1" class="grey--text caption">(+ {{ selectedSources.length - 1 }} других)</span>
                        </template>
                        <template v-slot:prepend-item>
                            <v-list-item ripple v-on:click="selectAllSources">
                                <v-list-item-action>
                                    <v-icon>{{ icon }}</v-icon>
                                </v-list-item-action>
                                <v-list-item-content>
                                    <v-list-item-title>Выбрать все</v-list-item-title>
                                </v-list-item-content>
                            </v-list-item>
                            <v-divider class="mt-2"></v-divider>
                        </template>
                    </v-select>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" text v-on:click="addTask(selectedAccessProfile, selectedSources)">Создать</v-btn>
                    <v-btn color="primary" text class="mr-2" v-on:click="closeDialog">Отмена</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
        <v-dialog v-model="confirmDialog" max-width="500" persistent>
            <v-card>
                <v-card-title>{{ confirmDialogText }}</v-card-title>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn text color="primary" v-on:click="applyConfirmDialog">Да</v-btn>
                    <v-btn text color="primary" v-on:click="closeConfirmDialog">Отмена</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-container>
</template>
<script src="./task.js"></script>