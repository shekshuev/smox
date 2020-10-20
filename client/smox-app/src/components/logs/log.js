import Vue from "vue";
import { getLogs } from "src/api/log";

export default Vue.component("logcomponent", 
{
    data: function()
    {
        return{
            loading: true,
            totalLogs: 0,
            options: [],
            logs: [],
            footerProps: {
                "items-per-page-options": [10, 30, 50, 100] 
            },
            headers: [
                {
                    text: "Message",
                    align: "start",
                    sortable: "false",
                    value: "message"
                },
                {
                    text: "Date",
                    align: "start",
                    sortable: "false",
                    value: "date"
                },
                {
                    text: "Type",
                    align: "start",
                    sortable: "false",
                    value: "type"
                },
            ]
        }
    }, 
    mounted: async function()
    {
        let data = await getLogs();
        this.logs = data.logs;
        this.totalLogs = data.count;
        this.loading = false;
    },
    watch: {
        logs: function(newList)
        {
            newList.map(log => log.date = new Date(log.date))
        }
    },
    methods: 
    {
        async updateOptions(options)
        {
            this.loading = true;
            this.logs = [];
            let data = await getLogs(options.itemsPerPage, options.itemsPerPage * (options.page - 1))
            this.logs = data.logs;
            this.totalLogs = data.count;
            this.loading = false;
        },
    }
});