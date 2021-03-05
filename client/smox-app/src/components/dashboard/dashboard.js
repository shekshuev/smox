import Vue from "vue";
import { mapState } from "vuex";
import Chart from "chart.js";
import colors from 'vuetify/lib/util/colors'

export default Vue.component("dashboard",
{
    data: function ()
    {
        return {

        }
    },
    mounted: function()
    {
        console.log(this.sources.map((s) => { return s }))
        let ctx = this.$refs.postcountchart.getContext('2d');
        new Chart(ctx, 
        {
            type: "bubble",
            data: {
                labels: this.sources.map((s) => { return s.name }), 
                datasets: [{
                    label: 'Посты',
                    data: this.sources.map((s) => { return s.posts_count }),
                    backgroundColor: colors.blue.darken1,
                    borderColor: colors.blue.darken5, 
                    borderWidth: 1
                }]
            }
        });
    },
    methods: 
    {
        getRandomSources: function () 
        {
            if (this.sources.length == 0)
                return [];
            let result = [];
            let index = Math.floor(Math.random() * this.sources.length);
            while (result.length < 3)
            {
                if (!result.includes(this.sources[index]))
                {
                    result.push(this.sources[index]);
                }
                index = Math.floor(Math.random() * this.sources.length);
            }
            return result;
        }
    },
    computed: 
    {
        ...mapState({
            sources: state => state.source.sources,
            accessProfiles: state => state.accessProfile.accessProfiles,
        }),

    }
});