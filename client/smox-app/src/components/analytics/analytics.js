import Vue from "vue";
import { mapState } from "vuex";
import { createTarget, deleteTarget } from "src/api/target";
import { DELETE_TARGET, CREATE_TARGET } from "src/store/modules/target/mutation_types";
import targetCard from "src/components/target/target.vue"

export default Vue.component("analytics",
{
    components: { targetCard },
    data: function()
    {
        return {
            snackbar: false,
            error: "",
            dialog: false,
            keywords: [],
            keyword: "",
            title: "Untitled",
            beginDate: new Date().toISOString().substr(0, 10),
            endDate: new Date().toISOString().substr(0, 10),
            step: 0
        }
    },
    methods: 
    {
        addKeyword()
        {
            if (this.keyword != "")
            {
                this.keywords.push(this.keyword);
                this.keyword = "";
            }
                
        },
        removeKeyword(word)
        {
            let index = this.keywords.indexOf(word);
            if (index != null)
                this.keywords.splice(index, 1);
        },
        async search()
        {
            if (this.keywords.length == 0)
                return;
            let result = await createTarget(this.title, this.keywords.join("|"), this.beginDate, this.endDate);
            if (result.success)
            {
                this.$store.dispatch(CREATE_TARGET, result.response.target);
                this.dialog = false;
                this.clearData();
            }
            else 
            {
                this.dialog = false;
                this.clearData();
                this.error = result.response.message;
                this.snackbar = true;
            }
        },
        async dropTarget(target)
        {
            if (await deleteTarget(target))
                this.$store.dispatch(DELETE_TARGET, target);
        },
        clearData()
        {
            this.keywords = [];
            this.keyword = "";
            this.title = "Untitled";
            this.beginDate = new Date().toISOString().substr(0, 10);
            this.endDate = new Date().toISOString().substr(0, 10);
            this.step = 0;
        }
    },
    computed: 
    {
        ...mapState({
            targets: state => state.target.targets
        })
    }
});