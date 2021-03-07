import axios from "axios";
import API_URL from "./base.js"

const url = `${API_URL}settings`;

export async function readDatabaseConnection ()  
{
    let response = await axios.get(url);
    if (response.status == 200 && response.data["success"])
        return response.data.response.db;
    else return null;
}

export async function updateDatatbaseConnection(db)
{
    let response = await axios.put(url, null, 
    {
        params: 
        {
            name: db.name,
            host: db.host,
            login: db.login,
            password: db.password
        }
    });
    if (response.status == 200)
        return true;
    else return false;
}