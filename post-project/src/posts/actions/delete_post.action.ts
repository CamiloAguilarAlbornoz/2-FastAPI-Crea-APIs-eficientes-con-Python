import { postApi } from "../../api/postApi";

interface Props {
    id_post: string
}

export const delete_post = async ({id_post}: Props) => {

    if(!id_post) throw new Error('ID is required');
    await postApi.delete(`/posts/${id_post}`)
}