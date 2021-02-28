<template>
    <v-card outlined max-height="260" min-height="260" v-bind:style="border">
        <v-card-title>
            <v-icon large left>mdi-vk</v-icon>
            <span class="title font-weight-light">Вконтакте</span>
            <v-spacer></v-spacer>
            <v-icon large v-bind:color="color">{{ icon }}</v-icon>
        </v-card-title>
        <v-card-text >
            <p class="text">{{ post.text }}</p>
            <span>{{ new Date(post.created_at).toLocaleDateString() + " " + new Date(post.created_at).toLocaleTimeString()  }}</span>
        </v-card-text>
        <v-card-actions>
            <v-list-item class="grow">
                <v-list-item-avatar color="grey darken-3">
                    <v-img class="elevation-6" :src="post.source.photo"></v-img>
                </v-list-item-avatar>
                <v-list-item-content>
                    <v-list-item-title>{{ post.source.name }}</v-list-item-title>
                </v-list-item-content>
                <v-list-item-content>
                    <v-btn target="_blank" text :href="'https://vk.com/wall' + post.owner_id + '_' + post.post_id">Ссылка</v-btn>
                </v-list-item-content>
                <v-row align="center" justify="end">
                    <v-icon class="mr-1">mdi-heart</v-icon>
                    <span class="subheading mr-2">{{ post.timestamps[post.timestamps.length - 1].likes_count }}</span>
                    <v-icon class="mr-1">mdi-share</v-icon>
                    <span class="subheading mr-2">{{ post.timestamps[post.timestamps.length - 1].reposts_count }}</span>
                    <v-icon class="mr-1">mdi-comment</v-icon>
                    <span class="subheading mr-2">{{ post.timestamps[post.timestamps.length - 1].comments_count }}</span>
                    <v-icon class="mr-1">mdi-eye</v-icon>
                    <span class="subheading">{{ post.timestamps[post.timestamps.length - 1].views_count }}</span>
                </v-row>
            </v-list-item>
        </v-card-actions>
    </v-card>
</template>
<style>
    .text 
    {
        display: -webkit-box;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;  
        overflow: hidden;
    }
</style>
<script src="./postcard.js"></script>