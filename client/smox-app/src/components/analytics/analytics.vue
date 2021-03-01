<template>
    <v-container>
        <v-row>
            <v-col cols="12" sm="4" lg="3" v-for="target in targets" v-bind:key="target.id">
                <targetCard v-bind:target="target" v-bind:onDeleteButtonClicked="() => dropTarget(target)"/>
            </v-col>    
        </v-row>      
        <v-dialog v-model="dialog" persistent scrollable max-width="600px">
            <template v-slot:activator="{ on, attrs }">
                <v-btn v-on="on" v-bind="attrs" color="primary" fab fixed bottom right>
                    <v-icon>mdi-plus</v-icon>
                </v-btn>
            </template>
            <v-card>
                <v-card-title>
                    <span class="headline">Формирование целевого объекта</span>
                </v-card-title>
                <v-card-text>
                    <v-stepper v-model="step" vertical class="stepper">
                        <v-stepper-items>
                            <v-stepper-step step=0 :complete="step > 0">Название</v-stepper-step>
                            <v-stepper-content step=0>
                                <v-text-field v-model="title" hide-details label="Название ЦО" single-line></v-text-field>
                                <v-btn v-if="title.length > 0" color="blue darken-1" text v-on:click="step = 1">Далее</v-btn>
                            </v-stepper-content>
                            <v-stepper-step step=1 :complete="step > 1">Ключевые слова</v-stepper-step>
                            <v-stepper-content step=1 >
                                <div class="stepper-content">
                                    <v-toolbar flat>
                                        <v-text-field @keyup.enter="addKeyword" v-model="keyword" hide-details label="Ключевые слова" single-line></v-text-field>
                                        <v-btn icon v-on:click="addKeyword">
                                            <v-icon>mdi-pencil-plus</v-icon>
                                        </v-btn>
                                    </v-toolbar>
                                    <v-chip-group column>
                                        <v-chip close v-on:click:close="removeKeyword(word)" v-for="(word, index) in keywords" :key="index">{{ word }}</v-chip>
                                    </v-chip-group>
                                    <v-btn v-if="keywords.length > 0" color="blue darken-1" text v-on:click="step = 2">Далее</v-btn>
                                    <v-btn color="blue darken-1" text v-on:click="step = 0">Назад</v-btn>
                                </div>
                            </v-stepper-content>
                            <v-stepper-step step=2 :complete="step > 2">Дата начала</v-stepper-step>
                            <v-stepper-content step=2>
                                <v-date-picker v-model="beginDate" full-width class="mt-4"></v-date-picker>
                                <v-btn color="blue darken-1" text v-on:click="step = 3">Далее</v-btn>
                                <v-btn color="blue darken-1" text v-on:click="step = 1">Назад</v-btn>
                            </v-stepper-content>
                            <v-stepper-step step=3 :complete="step > 3">Дата окончания</v-stepper-step>
                            <v-stepper-content step=3>
                                <v-date-picker v-model="endDate" full-width class="mt-4"></v-date-picker>
                                <v-btn color="blue darken-1" text v-on:click="step = 4">Далее</v-btn>
                                <v-btn color="blue darken-1" text v-on:click="step = 2">Назад</v-btn>
                            </v-stepper-content>
                            <v-stepper-step step=4 :complete="step > 4">Поиск</v-stepper-step>
                            <v-stepper-content step=4>
                                <v-chip-group>
                                    <v-chip v-for="(word, index) in keywords" :key="index">{{ word }}</v-chip>
                                </v-chip-group>
                                <v-chip-group>
                                    <v-chip>{{ beginDate }}</v-chip>
                                    <v-chip>{{ endDate }}</v-chip>
                                </v-chip-group>
                                <v-btn color="blue darken-1" text v-on:click="search"> Поиск</v-btn>
                                <v-btn color="blue darken-1" text v-on:click="step = 3">Назад</v-btn>
                            </v-stepper-content>
                        </v-stepper-items>
                    </v-stepper>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text v-on:click="dialog = false">Отмена</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-container>
</template>
<style>
    .add-btn
    {
        bottom: 0;
        position: absolute;
        margin: 0 0 48px 48px;
    }
    .stepper{
        box-shadow: none;
    }
    .stepper-content 
    {
        overflow-y: scroll;
        height: 100%
    }
</style>
<script src="./analytics.js"></script>