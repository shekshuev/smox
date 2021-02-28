import Vue from "vue";

export default Vue.component("postcard", 
{
    props: [ "post" ],
    data: function()
    {
        return {
            colors: [ "#F44336", "#2E7D32" ],
            icons: ["mdi-emoticon-neutral-outline", "mdi-emoticon-happy-outline"]
        }
    },
    mounted: function()
    {
        //console.log(this.post)
    },
    computed: 
    {
        border: function()
        {
            return this.post.value == -1 ? "border: 1px solid rgba(0, 0, 0, 0.12);" : "border: 1px solid " + this.colors[this.post.value] + ";";
        },
        icon: function()
        {
            return this.post.value == -1 ? "" : this.icons[this.post.value];
        },
        color: function()
        {
            return this.post.value == -1 ? "secondary" : this.colors[this.post.value];
        }
    }
});