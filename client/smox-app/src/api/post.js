import axios from "axios";
import API_URL from "./base.js"

const url = `${API_URL}post`;

export async function getPosts(count = 15, page = 1, startDate=null, endDate=null)
{
    let response = await axios.get(url, 
    {
        params: 
        {
            count: count,
            page: page, 
            start_date: startDate.getTime() / 1000,
            end_date: endDate.getTime() / 1000
        }
    });
    if (response.status == 200)
        return response.data.response;
    else return null;
}

export async function updatePost(post)
{
    let form = new FormData();
    form.append("id", post.id);
    form.append("postId", post.postId);
    form.append("ownerId", post.ownerId);
    form.append("fromId", post.fromId);
    form.append("sourceId", post.sourceId);
    form.append("postedDate", post.postedDate);
    form.append("text", post.text);
    form.append("class", post.class);
    let response = await axios.put("/api/post", form);
    if (response.status == 200)
        return true;
    else return false;
}