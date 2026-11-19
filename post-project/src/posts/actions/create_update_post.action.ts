import { postApi } from "../../api/postApi";
import type { Post } from "../../interfaces/post.interface";
import { sleep } from "../pages/post/ui/sleep";

export const create_update_post = async (postLike: Partial<Post>): Promise<Post> => {
  
    await sleep(1500)

    const {data} = postLike.id_post
    ? await postApi.put(`/posts/${postLike.id_post}`, postLike)
    : await postApi.post('/posts', postLike)

    return data
}
