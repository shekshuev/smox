import Vue from "vue";
import { mapState } from "vuex";
import { createTarget } from "src/api/target";

export default Vue.component("analytics",
{
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
            let target = 
            {
                keywords: this.keywords.join("|")
            };
            await createTarget(target);
        }
    },
    computed: 
    {
        ...mapState({
            targets: state => state.target.targets
        })
    }
});