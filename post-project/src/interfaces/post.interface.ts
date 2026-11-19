import type { Author } from "./author.interface";
import type { Tag } from "./tag.interface";

export interface Post {
    title:   string;
    content: string;
    tags:    Tag[];
    author:  Author;
    id_post: string;
}