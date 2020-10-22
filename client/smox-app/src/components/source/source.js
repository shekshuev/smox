import Vue from "vue";
import { mapState } from "vuex";
import { addSource, deleteSource } from "src/api/source";
import { ADD_SOURCE, DELETE_SOURCE } from "src/store/modules/source/mutation_types";
import sourceCard from "./sourcecard.vue";

export default Vue.component("sources",
{
    components: { sourceCard },
    data: function()
    {
        return {
            delay: 0,
            loading: false,
            dialog: false,
            request: "",
            source: null,
            headers:
            [
                {
                    text: "Название",
                    align: "center",
                    sortable: "true",
                    value: "name"
                },
                {
                    text: "Описание",
                    align: "start",
                    sortable: "false",
                    value: "description"
                },
                {
                    text: "",
                    align: "center",
                    sortable: "false",
                    value: "action"
                },
            ]
        }
    },
    watch:
    {
        request: async function (newRequest)
        {
            
            clearTimeout(this.delay);
            if (newRequest == "") return;
            this.delay = setTimeout(async () => 
            {
                this.loading = true;
                this.source = await addSource(newRequest);
                this.loading = false;
            }, 2000);
        }
    },
    computed: 
    {
        ...mapState({
            sources: state => state.source.sources
        })
    },
    methods: 
    {
        async deleteSource(source)
        {
            if (await deleteSource(source))
                this.$store.dispatch(DELETE_SOURCE, source);
        },
        addSourceToStore()
        {
            this.$store.dispatch(ADD_SOURCE, this.source);
            this.dialog = false;
        },
        cansel()
        {
            this.source = null;
            this.request = "";
        }
    }
});