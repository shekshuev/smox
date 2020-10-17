import Vue from "vue";
import loginComponent from "account/components/login/login.vue";
import registerComponent from "account/components/register/register.vue";

export default Vue.component("mainComponent",
{
    components: { loginComponent, registerComponent },
    data: function()
    {
        return {
            login: true
        }
    },
    methods: 
    {
        chooseRegisterOrLogin()
        {
            this.login = !this.login;
        }
    }
});