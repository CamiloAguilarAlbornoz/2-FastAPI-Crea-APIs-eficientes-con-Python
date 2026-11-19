import { Navigate } from "react-router"
import { CustomFooter } from "../../../components/custom/CustomFooter"
import { CustomHeader } from "../../../components/custom/CustomHeader"
import { usePost } from "../../hooks/usePost"
import { CustomFullScreenLoading } from "../../../components/custom/CustomFullScreenLoading"
import { CustomHeaderPost } from "../../components/CustomHeaderPost"
import { DeleteUpdateComponent } from "../../components/DeleteUpdateComponent"
import { DataAuthorComponent } from "../../components/DataAuthorComponent"

export const PostPage = () => {

    const {getQuery} = usePost()
    const {data: post, isError, isLoading} = getQuery

    if (isError) return (<Navigate to='/' />)
    if (isLoading || post === undefined) return (<CustomFullScreenLoading />)
    return (
        <>
            <CustomHeader />
            <div className="mx-auto max-w-6xl px-4 py-10 sm:px-6">
                <article className="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
                    
                    <CustomHeaderPost title = {post.title} tags = {post.tags || undefined} />

                    {
                        post.content !== undefined && ( 
                            <>
                                <div className="px-6 py-6 sm:px-10 sm:py-8">
                                    <div className="space-y-4">
                                        {post.content.split('\n\n').map((paragraph, index) => (
                                            <p key={index} className="text-slate-600 leading-relaxed">
                                            {paragraph}
                                            </p>
                                        ))}
                                    </div>
                                    <DataAuthorComponent name = {post.author.name_author} email = {post.author.email_author} />
                                </div>
                            </>
                        )
                    }

                    <DeleteUpdateComponent id_post = {post.id_post} />
                </article>
            </div>
            <CustomFooter />
        </>
    )
}
