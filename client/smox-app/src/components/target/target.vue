<template>
    <v-card shaped :color="colors[color]" light>
        <v-card-title>
            <span class="headline">{{ target.title }} </span>
            <v-spacer></v-spacer>
            <v-menu>
                <template v-slot:activator="{ on, attrs }">
                    <v-btn icon v-on="on" v-bind="attrs">
                        <v-icon>mdi-dots-vertical</v-icon>
                    </v-btn>
                </template>
                <v-list>
                    <v-list-item link>
                        <v-list-item-icon>
                            <v-icon>mdi-eye</v-icon>
                        </v-list-item-icon>
                        <v-list-item-title>Просмотр</v-list-item-title>       
                    </v-list-item>
                    <v-list-item link>
                        <v-list-item-icon>
                            <v-icon>mdi-pencil</v-icon>
                        </v-list-item-icon>
                        <v-list-item-title>Изменить</v-list-item-title>       
                    </v-list-item>
                    <v-list-item link v-on:click="dialog=true">
                        <v-list-item-icon>
                            <v-icon>mdi-delete</v-icon>
                        </v-list-item-icon>
                        <v-list-item-title>Удалить</v-list-item-title>
                    </v-list-item>
                </v-list>
            </v-menu>
        </v-card-title>
        <v-card-text>
            <v-chip-group column>
                <v-chip class="chip" v-bind:key="index" v-for="(word, index) in target.keywords.split('|')">{{ word }}</v-chip>
            </v-chip-group>
            <p>публикаций: {{target.posts_count}} с {{ new Date(target.begin_date).toLocaleDateString() }} по {{ new Date(target.end_date).toLocaleDateString()  }}</p>
            <p class="display-3">{{ Number.isInteger(target.result * 100) ? (target.result * 100) : (target.result * 100).toFixed(2) }}%</p>
        </v-card-text>
        <v-dialog v-model="dialog" persistent max-width="290">
            <v-card>
                <v-card-title class="headline">Удалить объект?</v-card-title>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" text @click="dialog = false">Отмена</v-btn>
                    <v-btn color="red" text @click="deleteTarget">Да, удалить</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-card>
</template>
<style>
.chip
{
    pointer-events: none;
}
</style>
<script src="./target.js"></script>