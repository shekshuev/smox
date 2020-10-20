<template>
    <v-card outlined>
        <v-img  v-bind:src="source.photo">
            <v-card-title>{{ source.name }}</v-card-title>
        </v-img>
        <v-card-text>{{ source.description }}</v-card-text>
        
        <v-card-actions>
            <slot name="actions" v-bind:source="source"></slot>
        </v-card-actions>
    </v-card>
</template>
<script src="./sourcecard.js"></script>