import axios from "axios";
import API_URL from "./base.js"

const url = `${API_URL}post`;

export async function getPosts(count = 100, offset = 0, target_id = 0)
{
    let response = await axios.get(url, 
    {
        params: 
        {
            count: count,
            offset: offset, 
            target_id: target_id
        }
    });
    if (response.status == 200)
        return response.data.response;
    else return null;
}

export async function filterPosts(target_id)
{
    let response = await axios.get(url, 
    {
        params: 
        {
            target_id: target_id
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