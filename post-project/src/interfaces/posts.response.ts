import type { Post } from "./post.interface";

export interface PostResponse {
    page:        number;
    per_page:    number;
    total:       number;
    total_pages: number;
    has_prev:    boolean;
    has_next:    boolean;
    order_by:    string;
    direction:   string;
    items:       Post[];
}