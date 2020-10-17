import Vue from "vue";
import { login } from "account/api/login";

export default Vue.component("loginComponent", 
{
    data: function()
    {
        return {
            username: "",
            password: "",
            loading: false,
            error: false,
            errorMessage: ""
        }
    },
    methods: 
    {
        async login()
        {
            this.error = false;
            this.loading = true;
            let result = await login(this.username, this.password);
            if (result.login == false)
            {
                this.error = true;
                this.errorMessage = result.error;
                this.loading = false;
            }
        }
    }
});