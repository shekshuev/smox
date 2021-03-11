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

export async function createTarget(title, keywords, beginDate, endDate)
{
    try 
    {
        let response = await axios.post(url, null, {
            params: {
                title: title,
                keywords: keywords,
                begin_date: beginDate,
                end_date: endDate
            }
        });
        if (response.status == 200)
            return response.data;
    }
    catch (error)
    {
        return error.response.data;
    }
}

export async function deleteTarget(target)
{
    let response = await axios.delete(url, 
    {
        params: 
        {
            id: target.id
        }
    });
    if (response.status == 200)
        return true;
    else false;
}