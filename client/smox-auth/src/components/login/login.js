import Vue from "vue";
import jwt_decode from "jwt-decode";
import { login } from "src/api/login";
import axios from "axios";

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
            else 
            {
                let obj = jwt_decode(result.token);
                axios.defaults.headers.Authorization = "Bearer " + result.token;
                localStorage.setItem("username", obj.identity.username);
                localStorage.setItem("token", result.token);
                window.location.href = "/";
            }
        }
    }
});