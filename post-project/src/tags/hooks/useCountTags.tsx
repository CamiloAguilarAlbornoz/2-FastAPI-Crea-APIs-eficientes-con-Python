import { useQuery } from "@tanstack/react-query"
import { get_count_tags } from "../actions/get_count_tags"

export const useCountTags = () => {

    return useQuery({
        queryKey: ['tags'],
        queryFn: get_count_tags,
        staleTime: 1000 * 60 * 5, // Mantiene 5 minutos los datos en cache para qu+e no consulte tanto al api
    })
}
