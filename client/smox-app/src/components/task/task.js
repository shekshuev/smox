import Vue from "vue";
import { mapState } from "vuex";
import { addTask, deleteTask, stopTask } from "src/api/task";
import { ADD_TASK, DELETE_TASK, UPDATE_TASK } from "src/store/modules/task/mutation_types";

export default Vue.component("tasks",
{
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
            rules: {
                accessProfile: [(v) => !!v || "Выберите профиль доступа!"],
                sources: [(v) => v.length > 0 || "Выберите хотя бы один источник!"]
            }
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
            if (this.selectedAccessProfile != null && this.selectedSources.length != 0)
            {
                let result = await addTask(accessProfile, sources);
                if (result != null)
                {
                    this.$store.dispatch(ADD_TASK, result);
                    this.selectedAccessProfile = null;
                    this.selectedSources = [];
                    this.closeDialog();
                }
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
        async stopTask(task)
        {
            let result = await stopTask(task.id);
            if (result != null)
            {
                this.$store.dispatch(UPDATE_TASK, result);
            } 
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