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

export async function searchSource(request, accessToken)
{
    let response = await axios.get(url,
    {
        params: 
        {
            request: request,
            access_token: accessToken
        }
    });
    if (response.status == 200)
        return response.data.response.source;
    else return null;
}

export async function createSource(source)
{
    let response = await axios.post(url, null, 
    {
        params: 
        {
            source_id: source.source_id,
            name: source.name,
            domain: source.domain,
            description: source.description,
            photo: source.photo
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