import axios from "axios";

export async function getLogs(count = 10, offset = 0)
{
    let response = await axios.get("/api/log?count=" + count + "&offset=" + offset);
    if (response.status == 200)
        return response.data;
    else return null;
}