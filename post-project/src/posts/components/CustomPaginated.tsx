import { ChevronLeft, ChevronRight } from "lucide-react"
import { useSearchParams } from "react-router"

interface Props {
    totalPages: number,
    hasPrev: boolean,
    hasNext: boolean
}

export const CustomPaginated = ({totalPages, hasPrev, hasNext}: Props) => {

    if (totalPages === 1) return (<></>)

    const[ searchParams, setSearchParams ] = useSearchParams()
    const queryPage = searchParams.get('page') || 1
    const normalizedPage = !isNaN(+queryPage) ? +queryPage : 1

    const handleNavegateInPagination = (page: number) => {
        searchParams.set('page', page.toString())
        setSearchParams(searchParams)
    }

    return (
        <>
            <nav className="mt-10 flex items-center justify-center gap-2" aria-label="Paginación">
                <button
                onClick={() => handleNavegateInPagination(normalizedPage - 1)}
                disabled={!hasPrev}
                className="inline-flex items-center gap-1 rounded-lg border border-slate-300 px-3 py-2 text-sm font-medium text-slate-700 hover:border-sky-400 hover:text-sky-600 disabled:cursor-not-allowed disabled:opacity-40 transition-colors"
                >
                    <ChevronLeft className="h-4 w-4" />
                    Anterior
                </button>

                {
                    Array.from({ length: totalPages }, (_, i) => i + 1).map((num) => (
                        <button
                        key={num}
                        onClick={() => handleNavegateInPagination(num)}
                        aria-current={num === normalizedPage ? 'page' : undefined}
                        className={`h-9 w-9 rounded-lg text-sm font-medium transition-colors ${
                        num === normalizedPage
                            ? 'bg-sky-600 text-white'
                            : 'border border-slate-300 text-slate-700 hover:border-sky-400 hover:text-sky-600'
                        }`}>
                            {num}
                        </button>
                    ))
                }
                
                <button
                onClick={() => handleNavegateInPagination(normalizedPage + 1)}
                disabled={!hasNext}
                className="inline-flex items-center gap-1 rounded-lg border border-slate-300 px-3 py-2 text-sm font-medium text-slate-700 hover:border-sky-400 hover:text-sky-600 disabled:cursor-not-allowed disabled:opacity-40 transition-colors"
                >
                    Siguiente
                    <ChevronRight className="h-4 w-4" />
                </button>
            </nav>
        </>
    )
}
