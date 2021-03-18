import Vue from "vue";
import { mapState } from "vuex";
import { getPosts } from "src/api/post";
import postCard from "./postcard.vue";
import InfiniteLoading from 'vue-infinite-loading';

//import { SET_OPTIONS, SET_START_DATE, SET_END_DATE } from "src/store/modules/post/mutation_types";

export default Vue.component("posts",
{
    title: "SMOX | Posts",
    components: { postCard, InfiniteLoading },
    data: function()
    {
        return {
            completed: false,
            totalPosts: 0,
            posts: [],
            modal: false,
            dates: [ ],
            target: null,
            count: 10,
            page: 0,
            loading: false
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
    methods: 
    {
        applyFilter: function()
        {
            this.$refs.inf.stateChanger.reset();
            this.page = 0;
            this.posts = []
            
        },
        clearFilter: function()
        {
            this.target = null;
            this.page = 0;
            this.$refs.inf.stateChanger.reset();
            this.posts = [];
        },
        infiniteHandler: async function(state)
        {
            let result = await getPosts(this.count, this.page * this.count, this.target == null ? 0 : this.target.id);
            if (result)
            {
                if (result.posts.length == 0)
                    state.complete();
                else 
                {
                    this.posts = this.posts.concat(result.posts);
                    this.page ++;
                    state.loaded();
                }
            }
        }
    }
});