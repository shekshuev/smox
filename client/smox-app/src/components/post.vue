<template>
    <v-container>
        <v-row>
            <v-col cols="12" sm="4">
                <v-card outlined>
                    <v-card-title>Фильтр</v-card-title>
                    <v-card-text>
                        <v-select
                            v-bind:items="targets"
                            outlined
                            dense
                            label="Целевой объект"
                            v-model="target"
                            item-text="title"
                            return-object
                        ></v-select>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="secondary" text v-on:click="clearFilter">Сброс</v-btn>
                        <v-btn color="primary" text v-on:click="applyFilter">Применить</v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
            <v-col cols="12" sm="8">
                <div>
                    <postcard
                        v-for="post in posts"
                        v-bind:key="post.id"
                        v-bind:post="post"
                        class="mb-3"
                        infinite-wrapper
                    ></postcard>
                    <infinite-loading
                        :force-use-infinite-wrapper="true"
                        ref="inf"
                        spinner="waveDots"
                        @infinite="infiniteHandler"
                    >
                        <div slot="spinner" v-if="posts.length == 0">
                            <v-card outlined v-for="i in [0, 1, 2]" v-bind:key="i" class="mb-3">
                                <v-card-text>
                                    <v-skeleton-loader
                                        type="list-item-avatar, list-item-three-line, card-heading"
                                    ></v-skeleton-loader>
                                </v-card-text>
                            </v-card>
                        </div>
                        <div slot="spinner" v-if="posts.length > 0">
                            <v-progress-circular
                                v-if="posts.length > 0"
                                indeterminate
                                color="primary"
                            ></v-progress-circular>
                        </div>
                        <div slot="no-more">
                            <span class="text--secondary">Загружены все публикации</span>
                        </div>
                        <div slot="no-results">
                            <span class="text--secondary">Нет публикаций по данному запросу</span>
                        </div>
                    </infinite-loading>
                </div>
            </v-col>
            <!--<v-col v-if="!loading" cols="12" sm="8">
                <infinite-loading spinner="waveDots">
                    <postcard v-for="post in posts" v-bind:key="post.id" v-bind:post="post" class="mb-3"></postcard>
                </infinite-loading>
            </v-col>
            <v-col v-if="posts == null || loading" cols="12" sm="8">
                <v-card outlined v-for="i in [0, 1, 2]" v-bind:key="i" class="mb-3">
                    <v-card-text>
                        <v-skeleton-loader type="list-item-avatar, list-item-three-line, card-heading"></v-skeleton-loader>
                    </v-card-text>
                </v-card>
            </v-col>-->
        </v-row>
    </v-container>
</template>
<script>
import Vue from "vue";
import { mapState } from "vuex";
import { getPosts } from "src/api/post";
import postCard from "./postcard.vue";
import InfiniteLoading from "vue-infinite-loading";

//import { SET_OPTIONS, SET_START_DATE, SET_END_DATE } from "src/store/modules/post/mutation_types";

export default Vue.component("posts", {
    title: "SMOX | Posts",
    components: { postCard, InfiniteLoading },
    data: function() {
        return {
            completed: false,
            totalPosts: 0,
            posts: [],
            modal: false,
            dates: [],
            target: null,
            count: 10,
            page: 0,
            loading: false,
        };
    },
    computed: {
        dateRangeText() {
            let formattedDates = this.dates.map((date) => {
                let [year, month, day] = date.split("-");
                return `${day}.${month}.${year}`;
            });
            return formattedDates.join(" ~ ");
        },
        ...mapState({
            options: (state) => state.post.options,
            startDate: (state) => state.post.startDate,
            endDate: (state) => state.post.endDate,
            targets: (state) => state.target.targets,
        }),
    },
    methods: {
        applyFilter: function() {
            this.$refs.inf.stateChanger.reset();
            this.page = 0;
            this.posts = [];
        },
        clearFilter: function() {
            this.target = null;
            this.page = 0;
            this.$refs.inf.stateChanger.reset();
            this.posts = [];
        },
        infiniteHandler: async function(state) {
            let result = await getPosts(this.count, this.page * this.count, this.target == null ? 0 : this.target.id);
            if (result) {
                if (result.posts.length == 0) state.complete();
                else {
                    this.posts = this.posts.concat(result.posts);
                    this.page++;
                    state.loaded();
                }
            }
        },
    },
});
</script>
