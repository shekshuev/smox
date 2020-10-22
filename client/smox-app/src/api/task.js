import axios from "axios";

export async function getTasks ()  
{
    let response = await axios.get("/api/task");
    if (response.status == 200)
        return response.data;
    else return null;
}

export async function addTask(accessProfile, sources)
{
    let form = new FormData();
    form.append("id", accessProfile.id);
    form.append("name", accessProfile.name);
    form.append("accessToken", accessProfile.accessToken);
    form.append("current", accessProfile.current);
    form.append("sources", JSON.stringify(sources));
    let response = await axios.post("/api/task", form);
    if (response.status == 200)
        return response.data;
    else return null;
}

export async function deleteTask(taskId)
{
    let response = await axios.delete("/api/task", { params: { id: taskId } });
    if (response.status == 200)
        return true;
    else return false;
}