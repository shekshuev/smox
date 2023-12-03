<template>
    <v-card outlined max-height="300" min-height="300" v-bind:style="border">
        <v-card-title>
            <v-icon large left>mdi-vk</v-icon>
            <span class="title font-weight-light">Вконтакте</span>
            <v-spacer></v-spacer>
            <v-icon large v-bind:color="color">{{ icon }}</v-icon>
        </v-card-title>
        <v-card-text>
            <p class="text">{{ post.text }}</p>
            <span>{{
                new Date(post.created_at).toLocaleDateString() + " " + new Date(post.created_at).toLocaleTimeString()
            }}</span>
            <v-icon class="mr-1 ml-4">mdi-heart</v-icon>
            <span class="subheading mr-2">{{ post.timestamps[post.timestamps.length - 1].likes_count }}</span>
            <v-icon class="mr-1">mdi-share</v-icon>
            <span class="subheading mr-2">{{ post.timestamps[post.timestamps.length - 1].reposts_count }}</span>
            <v-icon class="mr-1">mdi-comment</v-icon>
            <span class="subheading mr-2">{{ post.timestamps[post.timestamps.length - 1].comments_count }}</span>
            <v-icon class="mr-1">mdi-eye</v-icon>
            <span class="subheading">{{ post.timestamps[post.timestamps.length - 1].views_count }}</span>
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
                    <v-row>
                        <v-btn
                            text
                            class="ml-3"
                            @click="() => updateValue(1)"
                            :outlined="post.fit_value === 1"
                            :color="post.fit_value === 1 ? 'success' : 'secondary'"
                            ><v-icon>mdi-emoticon-happy-outline</v-icon></v-btn
                        >
                        <v-btn
                            text
                            class="ml-3"
                            @click="() => updateValue(0)"
                            :outlined="post.fit_value === 0"
                            :color="post.fit_value === 0 ? 'warning' : 'secondary'"
                            ><v-icon>mdi-emoticon-neutral-outline</v-icon></v-btn
                        >
                    </v-row>
                </v-list-item-content>
                <v-list-item-content>
                    <v-btn target="_blank" text :href="'https://vk.com/wall' + post.owner_id + '_' + post.post_id"
                        >Ссылка</v-btn
                    >
                </v-list-item-content>
            </v-list-item>
        </v-card-actions>
    </v-card>
</template>
<script>
import Vue from "vue";

export default Vue.component("postcard", {
    props: ["post"],
    data: function() {
        return {
            colors: ["#F44336", "#2E7D32"],
            icons: ["mdi-emoticon-neutral-outline", "mdi-emoticon-happy-outline"],
        };
    },
    mounted: function() {
        console.log(this.post);
    },
    computed: {
        border: function() {
            return this.post.value == -1
                ? "border: 1px solid rgba(0, 0, 0, 0.12);"
                : "border: 1px solid " + this.colors[this.post.value] + ";";
        },
        icon: function() {
            return this.post.value == -1 ? "" : this.icons[this.post.value];
        },
        color: function() {
            return this.post.value == -1 ? "secondary" : this.colors[this.post.value];
        },
    },
    methods: {
        updateValue(value) {
            this.$emit("change", { ...this.post, fit_value: value });
        },
    },
});
</script>
<style>
.text {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
}
</style>
