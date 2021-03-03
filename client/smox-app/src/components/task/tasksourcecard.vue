<template>
    <v-card outlined>
        <v-container>
            <v-row>
                <v-col sm="3">
                    <!--<sourceCard :source="taskSource.source"></sourceCard>-->
                </v-col>
                <v-col>
                    <v-card-text>Всего загружено: {{ taskSource.totalObjectsDownloaded }}</v-card-text>
                    <v-card-text>Смещение: {{ taskSource.offset }}</v-card-text>
                    <v-card-text>Количество загружаемых объектов: {{ taskSource.count }}</v-card-text>
                    <v-card-text>Начальное число объектов: {{ taskSource.beginCount }}</v-card-text>
                </v-col>
            </v-row>
        </v-container>
    </v-card>
</template>
<script src="./tasksourcecard.js"></script>