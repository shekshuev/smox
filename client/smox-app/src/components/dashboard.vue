<template>
    <v-container fluid>
        <v-row>
            <v-col cols="12" sm="4">
                <v-card outlined>
                    <v-card-title>Источники данных</v-card-title>
                    <v-card-text>
                        <v-list subheader rounded>
                            <v-list-item v-for="source in getRandomSources()" v-bind:key="source.id">
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
<script>
import Vue from "vue";
import { mapState } from "vuex";
import Chart from "chart.js";
import colors from "vuetify/lib/util/colors";

export default Vue.component("dashboard", {
    title: "SMOX | Dashboard",
    data: function() {
        return {};
    },
    mounted: function() {
        let ctx = this.$refs.postcountchart.getContext("2d");
        new Chart(ctx, {
            type: "bubble",
            data: {
                labels: this.sources.map((s) => {
                    return s.name;
                }),
                datasets: [
                    {
                        label: "Посты",
                        data: this.sources.map((s) => {
                            return s.posts_count;
                        }),
                        backgroundColor: colors.blue.darken1,
                        borderColor: colors.blue.darken5,
                        borderWidth: 1,
                    },
                ],
            },
        });
    },
    methods: {
        getRandomSources: function() {
            if (this.sources.length <= 3) return this.sources;
            let result = [];
            let index = Math.floor(Math.random() * this.sources.length);
            while (result.length < 3) {
                if (!result.includes(this.sources[index])) {
                    result.push(this.sources[index]);
                }
                index = Math.floor(Math.random() * this.sources.length);
            }
            return result;
        },
    },
    computed: {
        ...mapState({
            sources: (state) => state.source.sources,
            accessProfiles: (state) => state.accessProfile.accessProfiles,
        }),
    },
});
</script>
