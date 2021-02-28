<template>
    <v-container>
        <v-row>
            <v-col cols="12" sm="4">
                <v-card outlined>
                    <v-card-title>Фильтр</v-card-title>
                    <v-card-text>
                        <v-select v-bind:items="targets" outlined dense label="Целевой объект" v-model="target" item-text="title" return-object></v-select>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="secondary" text v-on:click="clearFilter">Сброс</v-btn>
                        <v-btn color="primary" text v-on:click="applyFilter">Применить</v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
            <v-col v-if="!loading" cols="12" sm="8">
                <v-virtual-scroll v-bind:bench="3" v-bind:items="posts" height="700" :item-height="270">
                    <template v-slot:default="post">
                        <postcard v-bind:post="post.item"></postcard>
                    </template>
                </v-virtual-scroll>
            </v-col>
            <v-col v-if="posts == null || loading" cols="12" sm="8">
                <v-card outlined v-for="i in [0, 1, 2]" v-bind:key="i" class="mb-3">
                    <v-card-text>
                        <v-skeleton-loader type="list-item-avatar, list-item-three-line, card-heading"></v-skeleton-loader>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>
<script src="./post.js"></script>