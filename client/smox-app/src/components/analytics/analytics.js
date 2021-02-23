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
            dialog: false,
            keywords: [],
            keyword: ""
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
            let target = 
            {
                keywords: this.keywords.join("|")
            };
            let result = await createTarget(target);
            if (result)
            {
                this.$store.dispatch(CREATE_TARGET, result);
                this.dialog = false;
            }
        },
        async dropTarget(target)
        {
            if (await deleteTarget(target))
                this.$store.dispatch(DELETE_TARGET, target);
        }
    },
    computed: 
    {
        ...mapState({
            targets: state => state.target.targets
        })
    }
});