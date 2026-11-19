import { Users } from "lucide-react";
import type { UseFormRegister } from "react-hook-form";
import type { Post } from "../../interfaces/post.interface";

interface Props {
    register: UseFormRegister<Post>
}

export const CustomAuthorsPost = ({register}: Props) => {
  return (
    <div>
        <label
            htmlFor="authors"
            className="mb-1.5 flex items-center gap-2 text-sm font-semibold text-slate-800">
            <Users className="h-4 w-4 text-blue-600" />
            Autores
        </label>
        <div
            className="flex flex-wrap items-center gap-2 rounded-lg border border-slate-300 px-2.5 py-2 transition-colors focus-within:border-blue-500 focus-within:ring-2 focus-within:ring-inset focus-within:ring-blue-200"
        >
            <input
            id="authorName"
            type="text"
            placeholder = "Escribe el nombre del autor..."
            className="flex-1 min-w-37.5 border-0 bg-transparent py-1 text-sm text-slate-900 placeholder-slate-400 outline-none"
            {
                ...register('author.name_author', {
                    required: true
                })
            }
            />
        </div>
        <div
            className="flex mt-2 flex-wrap items-center gap-2 rounded-lg border border-slate-300 px-2.5 py-2 transition-colors focus-within:border-blue-500 focus-within:ring-2 focus-within:ring-inset focus-within:ring-blue-200"
        >
            <input
            id="authorEmail"
            type="email"
            placeholder = "Escribe el correo electrónico del autor..."
            className="flex-1 min-w-37.5 border-0 bg-transparent py-1 text-sm text-slate-900 placeholder-slate-400 outline-none"
            {
                ...register('author.email_author', {
                    required: true
                })
            }
            />
        </div>
    </div>
  )
}
