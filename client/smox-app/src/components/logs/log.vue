<template>
    <v-container>
        <v-row>
            <v-col>
                <v-data-table 
                    :headers="headers" 
                    :items="logs" 
                    :loading="loading"
                    :server-items-length="totalLogs"
                    :footer-props="footerProps"
                    v-on:update:options="updateOptions">    
                </v-data-table>
            </v-col>
        </v-row>
    </v-container>
</template>
<script src="./log.js"></script>