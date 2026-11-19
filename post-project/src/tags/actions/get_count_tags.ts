import { postApi } from "../../api/postApi"
import type { TagsQuantity } from "../../interfaces/quantityTags.interface"

export const get_count_tags = async (): Promise<TagsQuantity[]> => {

    const {data} = await postApi.get<TagsQuantity[]>('/tags/count')
    return data
}