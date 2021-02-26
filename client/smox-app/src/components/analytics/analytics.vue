<template>
    <v-container>
        <v-row>
            <v-col cols="12" sm="4" v-for="target in targets" v-bind:key="target.id">
                <targetCard v-bind:target="target" v-bind:onDeleteButtonClicked="() => dropTarget(target)"/>
            </v-col>    
        </v-row>      
        <v-dialog v-model="dialog" persistent max-width="600px">
            <template v-slot:activator="{ on, attrs }">
                <v-btn v-on="on" v-bind="attrs" color="primary" fab fixed bottom right>
                    <v-icon>mdi-plus</v-icon>
                </v-btn>
            </template>
            <v-card>
                <v-card-title>
                    <span class="headline">Формирование целевого объекта</span>
                </v-card-title>
                <v-card-text>
                    <v-container>
                        <v-row>
                            <v-col cols="12" sm="12">
                                <v-toolbar flat>
                                    <v-text-field @keyup.enter="addKeyword" v-model="keyword" hide-details label="Ключевые слова" single-line></v-text-field>
                                    <v-btn icon v-on:click="addKeyword">
                                        <v-icon>mdi-magnify</v-icon>
                                    </v-btn>
                                </v-toolbar>
                                <v-chip-group>
                                    <v-chip close v-on:click:close="removeKeyword(word)" v-for="(word, index) in keywords" :key="index">{{ word }}</v-chip>
                                </v-chip-group>
                            </v-col>
                        </v-row>
                    </v-container>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text v-on:click="dialog = false">Отмена</v-btn>
                    <v-btn color="blue darken-1" text v-on:click="search">Поиск</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-container>
</template>
<style>
    .add-btn
    {
        bottom: 0;
        position: absolute;
        margin: 0 0 48px 48px;
    }
</style>
<script src="./analytics.js"></script>