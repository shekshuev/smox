import axios from "axios";

export async function getSources ()  
{
    let response = await axios.get("/api/source");
    if (response.status == 200)
        return response.data;
    else return null;
}

export async function searchSource(request)
{
    let response = await axios.get("/api/source_search?request=" + request);
    if (response.status == 200)
        return response.data;
    else return null;
}

export async function addSource(source)
{
    let form = new FormData();
    form.append("id", source.id);
    form.append("sourceId", source.sourceId);
    form.append("name", source.name);
    form.append("domain", source.domain);
    form.append("description", source.description);
    form.append("photo", source.photo);
    form.append("canBeDownloaded", source.canBeDownloaded);
    let response = await axios.post("/api/source", form);
    if (response.status == 200)
        return response.data;
    else return null;
}

export async function deleteSource(source)
{
    let response = await axios.delete("/api/source?id=" + source.id);
    if (response.status == 200)
        return true;
    else false;
}