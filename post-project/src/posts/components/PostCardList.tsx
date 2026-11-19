import type { Post } from "../../interfaces/post.interface"
import { PostCard } from "./PostCard"

interface Props {
    pagePosts: Post[]
}

export const PostCardList = ({pagePosts}: Props) => {

    return(
        <>
            <section className="min-w-0 flex-1">
                {pagePosts.length === 0 ? (
                    <div className="rounded-2xl border border-slate-200 bg-white p-12 text-center text-slate-500">
                    No se encontraron posts para tu búsqueda.
                    </div>
                ) : (
                    <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
                    {pagePosts.map((post) => (
                        <PostCard key={post.id_post} post={post} />
                    ))}
                    </div>
                )}
            </section>            
        </>
    )
}
