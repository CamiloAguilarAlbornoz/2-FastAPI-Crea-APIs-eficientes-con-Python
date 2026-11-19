import { Navigate, useNavigate, useParams } from "react-router";
import { CustomHeaderCreatePost } from "../../components/CustomHeaderCreatePost";
import { usePost } from "../../hooks/usePost";
import { CreateUpdatePostForm } from "../../components/CreateUpdatePostForm";
import type { Post } from "../../../interfaces/post.interface";
import { toast, Toaster } from "sonner";
import { CustomFooter } from "../../../components/custom/CustomFooter";
import { CustomHeader } from "../../../components/custom/CustomHeader";

export const CreatePost = () => {
  
  const{id_post} = useParams()
  const{createUpdateQuery, getQuery} = usePost()
  const navigate = useNavigate()
  const{isError, isPending} = createUpdateQuery
  const{data: post} = getQuery

  const handleSubmit = async (postLike: Partial<Post>) => {
    await createUpdateQuery.mutateAsync(postLike, {
      onSuccess: (data) => {
        toast.success('Post actualizado correctamente', {
          position: 'top-right'
        })
        navigate(`/post/${data.id_post}`)
      },
      onError: (error) => {
        console.error(error)
        toast.error('Error al actualizar el producto')
      }
    })
  }

  if (isError) return (<Navigate to='/' />);

  return (
    <>
      <Toaster theme='dark'/>
      <CustomHeader />
      <div className="min-h-screen bg-slate-50">
        <div className="mx-auto max-w-3xl px-4 py-10 sm:px-6 lg:px-8">
          <CustomHeaderCreatePost id_post={id_post} />
          <CreateUpdatePostForm post = {post} onSubmit = {handleSubmit} isPending = {isPending}/>
        </div>
      </div>
      <CustomFooter />
    </>
  );
}