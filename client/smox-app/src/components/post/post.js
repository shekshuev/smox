import Vue from "vue";
import { mapState } from "vuex";
import { getPosts, filterPosts } from "src/api/post";
import postCard from "./postcard.vue";
//import { SET_OPTIONS, SET_START_DATE, SET_END_DATE } from "src/store/modules/post/mutation_types";

export default Vue.component("posts",
{
    components: { postCard },
    data: function()
    {
        return {
            loading: true,
            totalPosts: 0,
            posts: [],
            modal: false,
            dates: [ ],
            target: null
        }
    },
    computed: {
        dateRangeText () 
        {
            let formattedDates = this.dates.map(date => 
            {
                let [year, month, day] = date.split("-");
                return `${day}.${month}.${year}`
            });
            return formattedDates.join(' ~ ')
        },
        ...mapState({
            options: state => state.post.options,
            startDate: state => state.post.startDate,
            endDate: state => state.post.endDate,
            targets: state => state.target.targets
        })
    },
    mounted: async function()
    {
        await this.loadPosts()
    },
    methods: 
    {
        loadPosts: async function()
        {
            this.loading = true;
            let result = await getPosts();
            if (result)
            {
                this.posts = result.posts;
                this.loading = false;
            }
        }, 
        applyFilter: async function()
        {
            if (this.target != null)
            {
                this.loading = true;
                let result = await filterPosts(this.target.id);
                if (result)
                {
                    this.posts = result.posts;
                    this.loading = false;
                }
            }
            
        },
        clearFilter: async function()
        {
            this.target = null;
            await this.loadPosts();
        }
    }
});