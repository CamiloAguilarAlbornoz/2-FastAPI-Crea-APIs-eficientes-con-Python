import { Search } from "lucide-react"
import { useSearchParams } from "react-router"
import { useRef, type KeyboardEvent } from "react"

export const CustomJumbotron = () => {

    const inputRef = useRef<HTMLInputElement>(null)

    const[searchParams, setSearchParams] = useSearchParams()

    const handleSearchChange = (e: KeyboardEvent<HTMLInputElement>) => {
        if (e.key === 'Enter') {
            if (inputRef.current !== null) {
                searchParams.set('search', inputRef.current.value)
                setSearchParams(searchParams)
            }
        }
    }

    return (
        <>
            <div className="mx-auto mt-8 max-w-xl">
                <div className="relative">
                    <Search className="absolute left-3.5 top-1/2 h-4 w-4 -translate-y-1/2 text-slate-400" />
                    <input
                    type="text"
                    ref={inputRef}
                    onKeyDown={(e) => handleSearchChange(e)}
                    placeholder="Buscar posts…"
                    className="w-full rounded-xl border border-slate-300 bg-white py-3 pl-10 pr-4 text-sm text-slate-900 placeholder:text-slate-400 focus:border-sky-500 focus:outline-none focus:ring-2 focus:ring-sky-100 transition"
                    />
                </div>
            </div>
        </>
    )
}
