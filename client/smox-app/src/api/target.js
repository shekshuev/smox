import axios from "axios";
import API_URL from "./base.js"

const url = `${API_URL}target`;

export async function readTargets()
{
    let response = await axios.get(url);
    if (response.status == 200)
        return response.data.response.targets;
    else return null;
}

export async function createTarget(target)
{
    let response = await axios.post(url, null, {
        params: {
            keywords: target.keywords
        }
    });
    if (response.status == 200)
        return response.data.response.target;
    else 
    {
        console.log(response.data)
        return null;
    }
}