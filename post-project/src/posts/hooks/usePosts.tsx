import { useQuery } from "@tanstack/react-query"
import { getPostByTagsAction, getPostsAction } from "../actions/get_posts.action"
import { useSearchParams } from "react-router"

export const usePosts = () => {

    const[ searchParams ] = useSearchParams()
    const page = searchParams.get('page') || 1
    const search = searchParams.get('search') || undefined
    const tags = searchParams.getAll('tags') || []

    const getAllByTextOrDefault = () => {
        return useQuery({
            queryKey: ['posts', {page, search}],
            queryFn: () => getPostsAction({page, search}),
            staleTime: 1000 * 60 * 5, // Mantiene 5 minutos los datos en cache para que no consulte tanto al api
        })
    }

    const getPostByTags = () => {
        return useQuery({
            queryKey: ['posts-tags', {tags}],
            queryFn: () => getPostByTagsAction({tags}),
            staleTime: 1000 * 60 * 5, // Mantiene 5 minutos los datos en cache para que no consulte tanto al api
        })
    }

    return {getAllByTextOrDefault, getPostByTags}
}
