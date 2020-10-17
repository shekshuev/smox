import Vue from "vue";
import { mapState } from "vuex";
import { getPosts, updatePost } from "application/api/post";
import postCard from "./postcard.vue";
import { SET_OPTIONS, SET_START_DATE, SET_END_DATE } from "application/store/modules/post/mutation_types";

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
            footerProps: {
                itemsPerPageOptions: [15, 30, 50, 100],
                showFirstLastPage: true,
                showCurrentPage: true
            },
            headers: [
                {
                    text: "PostId",
                    align: "start",
                    sortable: "false",
                    value: "postId"
                },
                {
                    text: "OwnerId",
                    align: "start",
                    sortable: "false",
                    value: "ownerId"
                },
                {
                    text: "FromId",
                    align: "start",
                    sortable: "false",
                    value: "fromId"
                },
                {
                    text: "Дата публикации",
                    align: "start",
                    sortable: "false",
                    value: "postedDate"
                },
                {
                    text: "Класс",
                    align: "start",
                    sortable: "false",
                    value: "class"
                }
            ]
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
            endDate: state => state.post.endDate
        })
    },
    watch: {
        posts: function(newList)
        {
            newList.map(post => post.postedDate = new Date(post.postedDate))
        }
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
        dateToStr(date)
        {
            let year = date.getFullYear();
            let month = (date.getMonth() + 1).toString().length == 1 ? `0${date.getMonth() + 1}` : date.getMonth() + 1;
            let day = date.getDate().toString().length == 1 ? `0${date.getDate()}` : date.getDate();
            return `${year}-${month}-${day}`;
        },
        async onDateSelected()
        {
            let newStartDate = this.dates[0] == null | undefined ? null : new Date(this.dates[0]);
            let newEndDate = this.dates[1] == null | undefined ? null : new Date(this.dates[1]);
            this.$store.dispatch(SET_START_DATE, newStartDate);
            this.$store.dispatch(SET_END_DATE, newEndDate);
            let newOptions = Object.assign({}, this.options);
            newOptions.page = 1;
            await this.updateOptions(newOptions);
            this.modal = false;
        },
        async onDateCanceled()
        {
            this.modal = false;
        },
        async updateOptions(options)
        {
            this.loading = true;
            this.posts = [];
            let data = await getPosts(options.itemsPerPage, options.itemsPerPage * (options.page - 1), this.startDate, this.endDate)
            this.posts = data.posts;
            this.totalPosts = data.count;
            this.loading = false;
            this.$store.dispatch(SET_OPTIONS, options);
        },
        async updatePost(post)
        {
            if (await updatePost(post) == false)
                post.class = 0;
        }
    }
});