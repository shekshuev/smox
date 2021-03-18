import Vue from "vue";

export default Vue.component("loadingscreen",
{
    props: [ "progress" ],
    data: function()
    {
        return {
            mainlogo: require("src/assets/mainlogo.svg")
        }
    }
})