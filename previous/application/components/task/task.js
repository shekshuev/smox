import Vue from "vue";
import { mapState } from "vuex";
import { addTask, deleteTask } from "application/api/task";
import { ADD_TASK, DELETE_TASK, UPDATE_TASK } from "application/store/modules/task/mutation_types";
import taskSourceCard from "./tasksourcecard.vue";

import * as signalR from "@microsoft/signalr";

export default Vue.component("tasks",
{
    components: { taskSourceCard },
    data: function()
    {
        return {
            confirmDialog: false,
            confirmDialogText: "",
            confirmDialogCallback: this.defaultConfirmDialogCallback,
            defaultConfirmDialogCallback: () => this.confirmDialog = false,
            hubConnection: null,
            dialog: false,
            selectedAccessProfile: null,
            selectedSources: [],
            headers:
            [
                {
                    text: "В процессе",
                    align: "center",
                    sortable: "true",
                    value: "isFinished"
                },
                {
                    text: "Дата и время начала",
                    align: "start",
                    sortable: "false",
                    value: "beginDate"
                },
                {
                    text: "Дата и время окончания",
                    align: "start",
                    sortable: "false",
                    value: "endDate"
                },
                {
                    text: "Запросов к API",
                    align: "start",
                    sortable: "false",
                    value: "requestsCount"
                },
                {
                    text: "Ошибка",
                    align: "start",
                    sortable: "false",
                    value: "isError"
                },
                {
                    text: "Действия",
                    align: "start",
                    sortable: "false",
                    value: "action"
                }
            ]
        }
    },
    created: function()
    {
        //this.hubConnection = new signalR.HubConnectionBuilder().withUrl("/taskhub").build();
        //this.hubConnection.on("Task", (task) => {
        //    this.$store.dispatch(UPDATE_TASK, task);
        //});
        //this.hubConnection.start();
    },
    destroyed: function()
    {
        //this.hubConnection.stop();
    },
    computed: 
    {
        ...mapState({
            tasks: state => state.task.tasks,
            accessProfiles: state => state.accessProfile.accessProfiles,
            sources: state => state.source.sources,
        }),
        icon () 
        {
            if (this.selectedSources.length == this.sources.length) 
                return 'mdi-close-box';
            else if (this.selectedSources.length > 0 && this.selectedSources.length != this.sources.length) 
                return 'mdi-minus-box';
            else return 'mdi-checkbox-blank-outline';
        }
    },
    methods: 
    {
        async addTask(accessProfile, sources)
        {
            let result = await addTask(accessProfile, sources);
            if (result != null)
            {
                this.$store.dispatch(ADD_TASK, result);
                this.selectedAccessProfile = null;
                this.selectedSources = [];
                this.closeDialog();
            }
        },
        async deleteTask(task)
        {
            let result = await deleteTask(task.id);
            if (result == true)
            {
                this.$store.dispatch(DELETE_TASK, task);
            }   
        },
        stopTask(task)
        {
            
        },
        selectAllSources()
        {
            if (this.selectedSources.length == 0)
                this.selectedSources = this.sources;
            else this.selectedSources = []
        },
        closeDialog()
        {
            this.dialog = false;
        },
        showConfirmDialog(text, callback)
        {
            this.confirmDialogText = text;
            this.confirmDialogCallback = callback;
            this.confirmDialog = true;
        },
        applyConfirmDialog()
        {
            if (this.confirmDialogCallback != null)
                this.confirmDialogCallback();
            this.closeConfirmDialog();
        },
        closeConfirmDialog()
        {
            this.confirmDialog = false;
            this.confirmDialogCallback = this.defaultConfirmDialogCallback;
        }
    }
});