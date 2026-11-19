import { FileText } from "lucide-react"
import type { FieldErrors, UseFormRegister } from "react-hook-form"
import type { Post } from "../../interfaces/post.interface"

interface Props {
    register: UseFormRegister<Post>,
    errors: FieldErrors<Post>
}

export const CustomTitlePost = ({register, errors}: Props) => {
  return (
    <div>
        <label
            htmlFor="title"
            className="mb-1.5 flex items-center gap-2 text-sm font-semibold text-slate-800"
        >
            <FileText className="h-4 w-4 text-blue-600" />
            Título
        </label>
        <input
            id="title"
            type="text"
            {
                ...register('title', {
                    required: true
                })
            }
            placeholder="Escribe un título atractivo..."
            className={`w-full rounded-lg border px-3.5 py-2.5 text-sm text-slate-900 placeholder-slate-400 transition-colors focus:outline-none focus:ring-2 focus:ring-inset ${
            errors.title
                ? "border-red-300 focus:border-red-400 focus:ring-red-200"
                : "border-slate-300 focus:border-blue-500 focus:ring-blue-200"
            }`}
        />
        {errors.title && (
            <p className="mt-1.5 text-xs text-red-600">El título es requerido</p>
        )}
    </div>
  )
}
