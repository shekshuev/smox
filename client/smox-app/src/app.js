import Vue from "vue";
import { LOAD_ACCESS_PROFILES } from "./store/modules/access_profile/mutation_types";
import { LOAD_SOURCES } from "./store/modules/source/mutation_types";
import { LOAD_TASKS } from "./store/modules/task/mutation_types";

export default Vue.component("app",
{
    data: function()
    {
        return {
            drawer: false
        }
    },
    created: function()
    {
        //this.$vuetify.theme.dark = true
        this.$store.dispatch(LOAD_ACCESS_PROFILES);
        this.$store.dispatch(LOAD_SOURCES);
        this.$store.dispatch(LOAD_TASKS);
    },
    methods: 
    {
        logout()
        {
            //window.location = "/account/logout";
            console.log("logout")
        }
    }
})