import axios from "axios";
import API_URL from "./base.js";

const url = `${API_URL}post`;

export async function getPosts(count = 100, offset = 0, target_id = 0) {
    let response = await axios.get(url, {
        params: {
            count: count,
            offset: offset,
            target_id: target_id,
        },
    });
    if (response.status == 200) return response.data.response;
    else return null;
}

export async function filterPosts(target_id) {
    let response = await axios.get(url, {
        params: {
            target_id: target_id,
        },
    });
    if (response.status == 200) return response.data.response;
    else return null;
}

export async function updatePost(post) {
    let form = new FormData();
    form.append("id", post.id);
    form.append("fit_value", post.fit_value);
    let response = await axios.put(url, form);
    if (response.status == 200) return response.data.response.post;
    else return false;
}
