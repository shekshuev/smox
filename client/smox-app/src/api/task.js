import axios from "axios";
import API_URL from "./base.js"

const url = `${API_URL}task`;

export async function getTasks ()  
{
    let response = await axios.get(url);
    console.log(response.data.response.tasks)
    if (response.status == 200)
        return response.data.response.tasks;
    else return null;
}

export async function addTask(accessProfile, sources)
{
    let response = await axios.post(url, null, 
    {
        params: 
        {
            access_profile_id: accessProfile.id,
            source_ids: sources.map(source => source.id).join(",")
        }
    });
    if (response.status == 200)
        return response.data.response.task;
    else return null;
}

export async function deleteTask(taskId)
{
    let response = await axios.delete(url, { params: { id: taskId } });
    if (response.status == 200)
        return true;
    else return false;
}