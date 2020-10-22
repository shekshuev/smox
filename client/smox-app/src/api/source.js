import axios from "axios";
import API_URL from "./base.js"

const url = `${API_URL}source`;

export async function getSources ()  
{
    let response = await axios.get(url);
    if (response.status == 200)
        return response.data.response.sources;
    else return null;
}

export async function addSource(request)
{
    let response = await axios.post(url, null, 
    {
        params: 
        {
            request: request
        }
    });
    if (response.status == 200)
        return response.data.response.source;
    else return null;
}

export async function deleteSource(source)
{
    let response = await axios.delete(url, 
    {
        params: 
        {
            id: source.id
        }
    });
    if (response.status == 200)
        return true;
    else false;
}