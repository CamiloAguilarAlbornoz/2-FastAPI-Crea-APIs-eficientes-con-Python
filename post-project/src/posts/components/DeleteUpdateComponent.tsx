import { Pencil, Trash2 } from "lucide-react"
import { useNavigate } from "react-router"

interface Props {
    id_post: string
}

export const DeleteUpdateComponent = ({id_post}: Props) => {

    const navigate = useNavigate()

    const onDelete = () => {
        navigate(`/post/delete/${id_post}`)
    }

    return (
        <>
            <section className="flex flex-wrap gap-3 border-t border-slate-100 px-6 py-5 sm:px-10">
                <button
                    onClick={() => navigate(`/${id_post}/edit`)}
                className="inline-flex items-center gap-2 rounded-lg bg-teal-600 px-5 py-2.5 font-medium text-white shadow-sm transition-all hover:bg-teal-700 hover:shadow-md active:scale-[0.98] focus:outline-none focus-visible:ring-2 focus-visible:ring-teal-500 focus-visible:ring-offset-2"
                >
                    <Pencil className="h-4 w-4" />
                    Editar
                </button>
                <button
                    onClick={onDelete}
                className="inline-flex items-center gap-2 rounded-lg bg-white px-5 py-2.5 font-medium text-red-600 border border-red-200 shadow-sm transition-all hover:bg-red-50 hover:border-red-300 active:scale-[0.98] focus:outline-none focus-visible:ring-2 focus-visible:ring-red-500 focus-visible:ring-offset-2"
                >
                    <Trash2 className="h-4 w-4" />
                    Eliminar
                </button>
            </section>
        </>
    )
}
