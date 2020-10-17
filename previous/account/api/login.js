import axios from "axios";

export async function login(username, password)  
{
    let form = new FormData();
    form.append("username", username);
    form.append("password", password);
    try
    {
        await axios.post("/account/login", form);
        window.location = "/";
    }
    catch (error)
    {

        if (error.response != (null || undefined) && error.response.status == 401)
            return {
                login: false,
                error: error.response.data.error
            }
        else     
            return {
                login: false,
                error: error.message
            }
    }
}