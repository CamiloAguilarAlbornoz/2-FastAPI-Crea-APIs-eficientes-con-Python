import { postApi } from "../../api/postApi";
import type { Post } from "../../interfaces/post.interface";
import type { PostResponse } from "../../interfaces/posts.response";

interface Options {
    page?: number | string;
    search?: string;
    tags?: string[]
}

export const getPostsAction = async ({page, search}: Options): Promise<PostResponse> => {

    const { data } = await postApi.get<PostResponse>('/posts', {
        params: {
            per_page: 9,
            page,
            search
        }
    })

    return data
}

export const getPostByTagsAction = async ({tags} : Options): Promise<Post[]> => {

    const {data} = await postApi.get<Post[]>('/posts/by-tags', {
        params: {
            tags
        },
        paramsSerializer: {
            indexes: null
        }
    })
    return data
}