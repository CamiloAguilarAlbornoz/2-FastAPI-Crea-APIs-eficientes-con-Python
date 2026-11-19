import { LogIn, UserPlus } from "lucide-react"
import { useNavigate } from "react-router"

export const CustomHeader = () => {

    const navigate = useNavigate();

    return (
        <>
            <header className="sticky top-0 z-10 border-b border-slate-200 bg-white/90 backdrop-blur">
                <div className="mx-auto flex max-w-6xl items-center justify-between gap-4 px-4 py-4 sm:px-6">
                <button
                    onClick={() => navigate('/')}
                    className="flex items-center gap-2 text-lg font-bold text-slate-900">
                    <span className="flex h-8 w-8 items-center justify-center rounded-lg bg-sky-600 text-white text-sm font-bold">
                        P
                    </span>
                    POSTS
                </button>
                <nav className="hidden items-center gap-6 text-sm font-medium text-slate-600 sm:flex">
                    <button onClick={() => navigate('/')} className="hover:text-sky-600 transition-colors">
                        Navegar por Título
                    </button>
                    <button onClick={() => navigate('/navigate-by-tags')} className="hover:text-sky-600 transition-colors">
                        Navegar por Tags
                    </button>
                    <button onClick={() => navigate('/new')} className="hover:text-sky-600 transition-colors">
                        Crear Post
                    </button>
                </nav>
                <div className="flex items-center gap-2">
                    <button className="inline-flex items-center gap-1.5 rounded-lg border border-slate-300 px-3 py-2 text-sm font-medium text-slate-700 hover:border-sky-400 hover:text-sky-600 transition-colors">
                    <LogIn className="h-4 w-4" />
                    Login
                    </button>
                    <button className="inline-flex items-center gap-1.5 rounded-lg bg-sky-600 px-3 py-2 text-sm font-medium text-white hover:bg-sky-700 transition-colors">
                    <UserPlus className="h-4 w-4" />
                    <span className="hidden sm:inline">Iniciar sesión</span>
                    </button>
                </div>
                </div>
            </header>
        </>
    )
}