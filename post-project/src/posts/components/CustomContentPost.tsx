import { FileText } from "lucide-react"
import type { Post } from "../../interfaces/post.interface"
import type { FieldErrors, UseFormRegister } from "react-hook-form"

interface Props {
    register: UseFormRegister<Post>,
    errors: FieldErrors<Post>,
    post?: Post
}

export const CustomContentPost = ({register, errors, post}: Props) => {
  return (
    <div>
        <label
            htmlFor="content"
            className="mb-1.5 flex items-center gap-2 text-sm font-semibold text-slate-800"
        >
            <FileText className="h-4 w-4 text-blue-600" />
            Contenido
        </label>
        <textarea
            id="content"
            {
                ...register('content', {
                    required: true
                })
            }
            placeholder="Escribe el contenido de tu publicación. Puede ser tan corto o largo como necesites..."
            rows={10}
            className={`w-full resize-y rounded-lg border px-3.5 py-2.5 text-sm leading-relaxed text-slate-900 placeholder-slate-400 transition-colors focus:outline-none focus:ring-2 focus:ring-inset ${
            errors.content
                ? "border-red-300 focus:border-red-400 focus:ring-red-200"
                : "border-slate-300 focus:border-blue-500 focus:ring-blue-200"
            }`}
        />
        {errors.content && (
            <p className="mt-1.5 text-xs text-red-600">El contenido es requerido</p>
        )}
        <p className="mt-1.5 text-xs text-slate-400">
            {post?.content.length} caracteres
        </p>
    </div>
  )
}
