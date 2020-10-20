<template>
    <v-container fluid>
        <v-row>
            <v-col>
                <v-data-table 
                    :headers="headers" 
                    :items="posts" 
                    :loading="loading"
                    :server-items-length="totalPosts"
                    :footer-props="footerProps"
                    :items-per-page="15"
                    :options="options"
                    v-on:update:options="updateOptions"
                    show-expand>
                    <template v-slot:expanded-item="{ headers, item }">
                        <td :colspan="headers.length">
                            <v-row>
                                <v-col>
                                    <postcard :post="item"/>
                                </v-col>
                            </v-row>
                        </td>
                    </template>  
                    <template v-slot:item.class="{ item }">
                        <v-radio-group v-model="item.class" row v-on:change="updatePost(item)">
                            <v-radio color="error" v-bind:value="-1" />
                            <v-radio color="secondary" v-bind:value="0" />
                            <v-radio color="success" v-bind:value="1" />
                        </v-radio-group>
                    </template> 
                    <template v-slot:item.postedDate="{ item }">
                        {{ new Date(item.postedDate).toLocaleDateString() + " " + new Date(item.postedDate).toLocaleTimeString() }}
                    </template>
                    <template v-slot:top>
                        <v-toolbar flat>
                            <v-toolbar-title>Загруженные посты</v-toolbar-title>
                            <v-spacer></v-spacer>
                            <v-col cols="2">
                                <v-dialog ref="dialog" v-model="modal" persistent width="290px" >
                                    <template v-slot:activator="{ on, attrs }">
                                        <v-text-field
                                            v-model="dateRangeText"
                                            label="Дата публикации"
                                            readonly
                                            v-bind="attrs"
                                            v-on="on"
                                        ></v-text-field> 
                                    </template>
                                    <v-date-picker v-model="dates" scrollable range>
                                        <v-spacer></v-spacer>
                                        <v-btn text color="primary" v-on:click="onDateCanceled">Отмена</v-btn>
                                        <v-btn text color="primary" v-on:click="onDateSelected">Поиск</v-btn>
                                    </v-date-picker>
                                </v-dialog>
                            </v-col>
                        </v-toolbar>    
                    </template> 
                </v-data-table>
            </v-col>
        </v-row>
    </v-container>
</template>
<script src="./post.js"></script>