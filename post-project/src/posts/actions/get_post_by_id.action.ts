import { postApi } from "../../api/postApi"
import type { Post } from "../../interfaces/post.interface"

interface Props {
    id_post: string;
    includes_content?: string | undefined;
}

export const get_post_by_id = async ({id_post, includes_content}: Props): Promise<Post> => {
    
    if(!id_post) throw new Error('ID is required');
    const with_content = (includes_content === 'true' || includes_content === 'false') ? includes_content : undefined

    const id = !isNaN(+id_post) ? id_post : 0

    const { data } = await postApi.get<Post>(`/posts/${id}`, {
        params: {
            includes_content: with_content
        }
    })
    return {...data}
}