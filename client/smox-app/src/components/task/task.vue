<template>
    <v-container>
        <v-row>
            <v-col>
                <v-data-table v-bind:headers="headers" v-bind:items="tasks" show-expand>
                    <template v-slot:item.isFinished="{ item }">
                        {{ !item.is_finished }}
                    </template>
                    <template v-slot:item.beginDate="{ item }">
                        {{ new Date(item.begin_datetime).toLocaleDateString() + " " + new Date(item.begin_datetime).toLocaleTimeString() }}
                    </template>
                    <template v-slot:item.endDate="{ item }">
                        {{  item.end_datetime == null ? "не окончено" : new Date(item.end_datetime).toLocaleDateString() + " " + new Date(item.endDate).toLocaleTimeString() }}
                    </template>
                    <template v-slot:item.action="{ item }">
                        <v-btn icon><v-icon v-on:click="stopTask(item)">mdi-stop</v-icon></v-btn>
                        <v-btn icon><v-icon v-on:click="showConfirmDialog('Удалить выбранный элемент?', () => deleteTask(item))">mdi-delete</v-icon></v-btn>
                    </template>
                    <template v-slot:expanded-item="{ headers, item }">
                        <td :colspan="headers.length">
                            <v-container>
                                <v-row v-for="source in item.task_sources" :key="source.id">
                                    <v-col>
                                        <taskSourceCard :taskSource="source"></taskSourceCard>
                                    </v-col>
                                </v-row>
                            </v-container>
                        </td>
                    </template>
                    <template v-slot:top>
                        <v-toolbar flat>
                            <v-toolbar-title>Задания</v-toolbar-title>
                            <v-spacer></v-spacer>
                            <v-dialog id="newTaskDialog" v-model="dialog" max-width="600px" persistent>
                                <template v-slot:activator="{ on }">
                                    <v-btn color="primary" dark class="mb-2" v-on="on">Новое</v-btn>
                                </template>
                                <v-card>
                                    <v-card-title>
                                        <span class="headline">Новый источник</span>
                                    </v-card-title>
                                    <v-card-text>
                                        <v-container>
                                            <v-row>
                                                <v-col>
                                                    <v-select v-model="selectedAccessProfile" :items="accessProfiles" label="Профиль доступа">
                                                        <template v-slot:selection="{ item, on }">
                                                            <v-list-item v-on="on">{{ item.name }}</v-list-item>
                                                        </template>
                                                        <template v-slot:item="{ item, on }">
                                                            <v-list-item v-on="on">{{ item.name }}</v-list-item>
                                                        </template>
                                                    </v-select>
                                                </v-col>
                                            </v-row>
                                            <v-row>
                                                <v-col> 
                                                    <v-select v-model="selectedSources" :items="sources" return-object item-text="name" label="Источники" multiple chips>
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
                                                </v-col>
                                            </v-row>
                                            <v-row>
                                                <v-col class="d-flex flex-row-reverse">
                                                    <v-btn color="primary" v-on:click="addTask(selectedAccessProfile, selectedSources)">Создать</v-btn>
                                                    <v-btn color="secondary" class="mr-2" v-on:click="closeDialog">Отмена</v-btn>
                                                </v-col>
                                            </v-row>
                                        </v-container>
                                    </v-card-text>
                                </v-card>
                            </v-dialog>
                        </v-toolbar>
                        
                    </template>
                </v-data-table>
            </v-col>
        </v-row>
        <v-dialog v-model="confirmDialog" max-width="500" persistent>
            <v-card>
                <v-card-title>{{ confirmDialogText }}</v-card-title>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn text v-on:click="applyConfirmDialog">Удалить</v-btn>
                    <v-btn text v-on:click="closeConfirmDialog">Отмена</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-container>
</template>
<script src="./task.js"></script>