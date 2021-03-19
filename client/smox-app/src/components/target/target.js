import Vue from "vue";

export default Vue.component("targetcard",
{
    props: ["target", "onDeleteButtonClicked"],
    data: function()
    {
        return {
            dialog: false,
            colors: ["#F44336", "#FF6E40", "#FF9800", "#FFC107", "#FFEB3B", "#FFEB3B", "#CDDC39", "#8BC34A", "#4CAF50", "#2E7D32", "#2E7D32"],
            color: this.toFixed(this.target.result, 1) * 10
        }
    },
    methods: 
    {
        deleteTarget: async function()
        {
            if (this.onDeleteButtonClicked)
            {
                await this.onDeleteButtonClicked()
            }
        },
        toFixed: function (num, fixed) {
            fixed = fixed || 0;
            fixed = Math.pow(10, fixed);
            return Math.floor(num * fixed) / fixed;
        }
    }
})