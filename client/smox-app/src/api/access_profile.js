import axios from "axios";
import API_URL from "./base.js"

const url = `${API_URL}access_profile`;

export async function getProfiles ()  
{
    let response = await axios.get(url);
    if (response.status == 200 && response.data["success"])
        return response.data.response.access_profiles;
    else return null;
}

export async function addProfile(profile)
{
    let response = await axios.post(url, null, {
        params: {
            name: profile.name,
            access_token: profile.accessToken
        }
    });
    if (response.status == 200)
        return response.data.response.access_profile;
    else 
    {
        console.log(response.data)
        return null;
    }
}

export async function deleteProfile(profile)
{
    let response = await axios.delete(url, {
        params: {
            id: profile.id
        }
    });
    if (response.status == 200)
        return true;
    else return false;
}