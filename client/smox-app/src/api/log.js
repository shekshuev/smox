import axios from "axios";
import API_URL from "./base.js"

const url = `${API_URL}log`;

export async function getLogs(count = 10, page = 1)
{
    let response = await axios.get(url, 
    {
        params: {
            count: count,
            page: page
        }
    });
    if (response.status == 200)
        return response.data.response;
    else return null;
}