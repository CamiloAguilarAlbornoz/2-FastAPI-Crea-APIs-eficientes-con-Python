import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query"
import { useParams, useSearchParams } from "react-router"
import { get_post_by_id } from "../actions/get_post_by_id.action"
import { delete_post } from "../actions/delete_post.action"
import { toast } from "sonner"
import { create_update_post } from "../actions/create_update_post.action"
import type { Post } from "../../interfaces/post.interface"

export const usePost = () => {

    const{id_post} = useParams()

    const queryClient = useQueryClient()

    const[searchParams, setSearchParams] = useSearchParams()
    let includes_content = searchParams.get('includes_content') || undefined

    if (includes_content !== undefined) {
        if (includes_content !== 'true' && includes_content !== 'false') {
            const newSearchParams = new URLSearchParams(searchParams)
            newSearchParams.delete('includes_content')
            setSearchParams(newSearchParams)
            includes_content = undefined
        }
    }

    const getQuery = useQuery({
        queryKey: ['posts', {id_post}],
        queryFn: () => {
            if (!id_post) throw new Error('ID is required')
            return get_post_by_id({id_post, includes_content})
        },
        staleTime: 1000 * 60 * 5, // Mantiene 5 minutos los datos en cache para qu+e no consulte tanto al api
    })

    const deleteQuery = useMutation({
        mutationFn: () => {
            if (!id_post) throw new Error('ID is required')
            return delete_post({id_post})
        },
        onSuccess: () => {
            queryClient.invalidateQueries({
                queryKey: ['posts']
            })
            toast.success('Post eliminado correctamente', {
                position: "top-right"
            })
        },
        onError: () => {
            toast.error('No se pudo eliminar el post')
        }
    })

    const createUpdateQuery = useMutation({
        mutationFn: create_update_post,
        onSuccess: (post: Post) => {
            
            // Invalidar cache
            queryClient.invalidateQueries({queryKey: ['posts']})

            // Actualizar querydata
            queryClient.setQueryData(['posts', {id_post: post.id_post}], post)
        }
    })

    return {getQuery, deleteQuery, createUpdateQuery}
}
