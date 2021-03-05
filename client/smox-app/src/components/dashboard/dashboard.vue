<template>
    <v-container fluid>
        <v-row>
            <v-col cols="12" sm="4">
                <v-card outlined>
                    <v-card-title>Источники данных</v-card-title>
                    <v-card-text>
                        <v-list subheader rounded>
                            <v-list-item v-for="source in getRandomSources()" v-bind:key="source.id" >
                                <v-list-item-avatar>
                                    <v-img :src="source.photo"></v-img>
                                </v-list-item-avatar>
                                <v-list-item-content>
                                    <v-list-item-title>{{ source.name }}</v-list-item-title>
                                    <v-list-item-subtitle>{{ source.description }}</v-list-item-subtitle>
                                </v-list-item-content>
                            </v-list-item>
                            <v-subheader v-if="sources.length > 3">и еще {{ sources.length - 3 }}</v-subheader>
                        </v-list>
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col cols="12" sm="8">
                <v-card outlined>
                    <v-card-title>Публикации</v-card-title>
                    <canvas ref="postcountchart"></canvas>
                </v-card>
            </v-col>
        </v-row>
        
    </v-container>
</template>
<script src="./dashboard.js"></script>