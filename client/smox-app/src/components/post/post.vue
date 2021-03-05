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
            <v-col cols="12" sm="8" >
                <div >
                    <postcard v-for="post in posts" v-bind:key="post.id" v-bind:post="post" class="mb-3" infinite-wrapper></postcard>
                    <infinite-loading :force-use-infinite-wrapper="true" ref="inf" spinner="waveDots" @infinite="infiniteHandler">
                        <div slot="spinner" v-if="posts.length == 0">
                            <v-card outlined v-for="i in [0, 1, 2]" v-bind:key="i" class="mb-3">
                                <v-card-text>
                                    <v-skeleton-loader type="list-item-avatar, list-item-three-line, card-heading"></v-skeleton-loader>
                                </v-card-text>
                            </v-card>
                        </div>
                        <div slot="spinner" v-if="posts.length > 0">
                            <v-progress-circular v-if="posts.length>0" indeterminate color="primary"></v-progress-circular>
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
<script src="./post.js"></script>