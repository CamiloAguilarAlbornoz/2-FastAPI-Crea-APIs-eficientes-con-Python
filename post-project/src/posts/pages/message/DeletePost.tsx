import { AlertTriangle, Check, X } from "lucide-react"
import { Navigate, useNavigate, useParams } from "react-router"
import { usePost } from "../../hooks/usePost"
import { sleep } from "../post/ui/sleep"

export const DeletePost = () => {

    const {id_post} = useParams()
    const navigate = useNavigate()
    const {deleteQuery} = usePost()
    const {mutateAsync} = deleteQuery

    if (id_post === undefined) return (<Navigate to='/' />)

    const handlerCalelDeletPost = () => {
        navigate(`/post/${id_post}`)
    }

    const handlerDeletePost = async () => {
        await mutateAsync()
        await sleep(1500)
        navigate('/')
    }

    return (
        <div className="min-h-screen bg-gray-100 flex items-center justify-center px-4">
            <div className="bg-white rounded-2xl shadow-xl max-w-sm w-full p-8 text-center">
                <div className="mx-auto mb-4 flex h-14 w-14 items-center justify-center rounded-full bg-red-100">
                    <AlertTriangle className="h-7 w-7 text-red-600" aria-hidden="true" />
                </div>
                <h1 className="text-xl font-semibold text-gray-900">
                    ¿Estás seguro de eliminar el post?
                </h1>
                <p className="mt-2 text-sm leading-relaxed text-gray-600">
                    Esta acción no se puede deshacer.
                </p>
                <div className="mt-6 flex flex-col sm:flex-row gap-3">
                    <button
                        type="button"
                        onClick={handlerDeletePost}
                        className="flex flex-1 items-center justify-center gap-2 rounded-xl bg-red-600 px-5 py-3 text-sm font-semibold text-white transition-colors duration-200 hover:bg-red-700 focus:outline-none focus-visible:ring-2 focus-visible:ring-red-600 focus-visible:ring-offset-2"
                    >
                        <Check className="h-4 w-4" aria-hidden="true" />
                        Aceptar
                    </button>
                    <button
                        type="button"
                        onClick={handlerCalelDeletPost}
                        className="flex flex-1 items-center justify-center gap-2 rounded-xl bg-white px-5 py-3 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-300 transition-colors duration-200 hover:bg-gray-100 focus:outline-none focus-visible:ring-2 focus-visible:ring-gray-900 focus-visible:ring-offset-2"
                    >
                        <X className="h-4 w-4" aria-hidden="true" />
                        Cancelar
                    </button>
                </div>
            </div>
        </div>
    )
}
