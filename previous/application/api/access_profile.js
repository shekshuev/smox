import axios from "axios";

export async function getProfiles ()  
{
    let response = await axios.get("/api/access_profiles");
    if (response.status == 200)
        return response.data;
    else return null;
}

export async function addProfile(profile)
{
    let form = new FormData();
    form.append("id", profile.id);
    form.append("name", profile.name);
    form.append("accessToken", profile.accessToken);
    form.append("current", profile.current);
    let response = await axios.post("/api/access_profile", form);
    if (response.status == 200)
        return response.data;
    else return null;
}

export async function deleteProfile(profile)
{
    let response = await axios.delete("/api/access_profile?id=" + profile.id);
    if (response.status == 200)
        return true;
    else return false;
}