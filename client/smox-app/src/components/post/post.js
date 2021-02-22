import Vue from "vue";
import { mapState } from "vuex";
//import { getPosts, updatePost } from "src/api/post";
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
        })
    },
    mounted: function()
    {
        if (this.startDate)
        {
            this.dates.push(this.dateToStr(this.startDate))
            if (this.endDate)
            {
                this.dates.push(this.dateToStr(this.endDate))
            }
        }
    },
    methods: 
    {

    }
});