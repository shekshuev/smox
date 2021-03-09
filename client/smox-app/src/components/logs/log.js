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
                    text: "Datetime",
                    align: "start",
                    sortable: "false",
                    value: "datetime"
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
            if (newList)
                newList.map(log => log.datetime = new Date(log.datetime))
        }
    },
    methods: 
    {
        async updateOptions(options)
        {
            this.loading = true;
            this.logs = [];
            let data = await getLogs(options.itemsPerPage, options.page)
            this.logs = data.logs;
            this.totalLogs = data.count;
            this.loading = false;
        },
    }
});