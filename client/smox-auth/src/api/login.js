import axios from "axios";
import API_URL from "./base.js"

const url = `${API_URL}login`;

export async function login(username, password)  
{
    try
    {
        let response = await axios.post(url, null, 
        {
            params: 
            {
                username: username,
                password: password
            }
        });
        if (response.status == 200)
        {
            return {
                login: true,
                token: response.data.response.token
            };
        }
        else throw new Error("Somthing wrong happined");
    }
    catch (error)
    {
        if (error.response.status == 401)
        {
            return {
                login: false,
                error: error.response.data.response.message
            };
        }
        else     
            return {
                login: false,
                error: error.message
            };
    }
}