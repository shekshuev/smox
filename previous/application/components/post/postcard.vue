<template>
    <v-card outlined>
        <v-card-title>
            <v-icon large left>mdi-vk</v-icon>
            <span class="title font-weight-light">Вконтакте</span>
        </v-card-title>
        <v-card-text>
            {{ post.text }}
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
                    <v-btn target="_blank" text :href="'https://vk.com/wall' + post.ownerId + '_' + post.postId">Ссылка</v-btn>
                </v-list-item-content>
                <v-row align="center" justify="end">
                    <v-icon class="mr-1">mdi-heart</v-icon>
                    <span class="subheading mr-2">{{ post.timeStamps[post.timeStamps.length - 1].likesCount }}</span>
                    <v-icon class="mr-1">mdi-share</v-icon>
                    <span class="subheading mr-2">{{ post.timeStamps[post.timeStamps.length - 1].repostsCount }}</span>
                    <v-icon class="mr-1">mdi-comment</v-icon>
                    <span class="subheading mr-2">{{ post.timeStamps[post.timeStamps.length - 1].commentsCount }}</span>
                    <v-icon class="mr-1">mdi-eye</v-icon>
                    <span class="subheading">{{ post.timeStamps[post.timeStamps.length - 1].viewsCount }}</span>
                </v-row>
            </v-list-item>
        </v-card-actions>
    </v-card>
</template>
<script src="./postcard.js"></script>