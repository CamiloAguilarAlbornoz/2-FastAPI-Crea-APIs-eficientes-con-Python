import { FileText } from "lucide-react"

interface Props {
  id_post?: string
}

export const CustomHeaderCreatePost = ({id_post}: Props) => {

  const title = id_post === undefined ? 'Crear nueva publicación' : 'Actualizar publicación'
  const message = id_post === undefined ? 'Completa los campos para crear un nuevo post.' : 'Completa los campos para actualizar un post existente.'

  return (
    <>
      <div className="mb-8">
          <div className="flex items-center gap-3">
            <div className="flex h-11 w-11 items-center justify-center rounded-xl bg-blue-600 text-white shadow-sm">
              <FileText className="h-6 w-6" />
            </div>
            <div>
              <h1 className="text-2xl font-bold tracking-tight text-slate-900">
                {title}
              </h1>
              <p className="mt-1 text-sm text-slate-500">
                {message}
              </p>
            </div>
          </div>
        </div>
    </>
  )
}
