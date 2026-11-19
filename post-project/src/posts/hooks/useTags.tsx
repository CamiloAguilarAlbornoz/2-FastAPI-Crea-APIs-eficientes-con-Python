import { useCountTags } from "../../tags/hooks/useCountTags";
import { useSearchParams } from "react-router";

export const useTags = () => {

    const {data: tags} = useCountTags()
    const[searchParams, setSearchParams] = useSearchParams([])
    const firtsTags = searchParams.getAll('tags')
    
    const toggleTag = (tag: string) => {
        if (searchParams.getAll('tags').includes(tag)) {
            const newSearchParams = new URLSearchParams(searchParams)
            newSearchParams.delete('tags', tag)
            setSearchParams(newSearchParams)
            return
        }
        searchParams.append('tags', tag)
        setSearchParams(searchParams)
    }

    return {
        tags,
        firtsTags,
        toggleTag
    }
}
