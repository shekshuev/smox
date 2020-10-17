import axios from "axios";
import { off } from "process";

export async function getPosts(count = 15, offset = 0, startDate=null, endDate=null)
{
    let response = await axios.get("/api/post", 
    {
        params: 
        {
            count: count,
            offset: offset, 
            startDate: startDate,
            endDate: endDate
        }
    });
    if (response.status == 200)
        return response.data;
    else return null;
}

export async function updatePost(post)
{
    console.log(post)
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