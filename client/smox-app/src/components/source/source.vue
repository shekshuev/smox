<template>
    <v-container fluid>
        <v-row>
            <v-col>
                <v-data-table v-bind:headers="headers" v-bind:items="sources">
                    <template v-slot:item.action="{ item }">
                        <v-btn icon><v-icon v-on:click="deleteSource(item)">mdi-delete</v-icon></v-btn>
                    </template>
                    <template v-slot:top>
                        <v-toolbar flat>
                            <v-toolbar-title>Источники данных</v-toolbar-title>
                            <v-spacer></v-spacer>
                            <v-dialog v-model="dialog" max-width="600px">
                                <template v-slot:activator="{ on }">
                                    <v-btn color="primary" dark class="mb-2" v-on="on">Новый источник</v-btn>
                                </template>
                                <v-card>
                                    <v-card-title>
                                        <span class="headline">Новый источник</span>
                                    </v-card-title>
                                    <v-card-text>
                                        <v-container>
                                            <v-row>
                                                <v-col>
                                                    <v-text-field v-model="request" label="Id или домен">
                                                        <template v-slot:append>
                                                            <v-progress-circular v-if="loading" indeterminate size="25"></v-progress-circular>
                                                        </template>
                                                    </v-text-field>
                                                </v-col>
                                            </v-row>
                                            <v-row v-if="source != null">
                                                <v-col>
                                                    <sourceCard :source="source">
                                                        <template v-slot:actions="{}">
                                                            <v-spacer></v-spacer>
                                                            <v-btn text v-on:click="cansel">Cansel</v-btn>
                                                            <v-btn text v-on:click="addSourceToStore">Save</v-btn>
                                                        </template>
                                                    </sourceCard>
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
    </v-container>
</template>
<script src="./source.js"></script>