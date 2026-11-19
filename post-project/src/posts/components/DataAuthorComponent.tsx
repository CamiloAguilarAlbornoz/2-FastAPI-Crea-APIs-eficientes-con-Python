import { Mail, User } from "lucide-react"

interface Props {
    name: string;
    email: string;
}

export const DataAuthorComponent = ({name, email}: Props) => {

    return (
        <>
            <div className="mt-8 flex items-center gap-4 rounded-xl bg-slate-50 border border-slate-200 p-4">
                <div className="flex h-11 w-11 shrink-0 items-center justify-center rounded-full bg-slate-800 text-white">
                    <User className="h-5 w-5" />
                </div>
                <div className="min-w-0">
                    <p className="font-semibold text-slate-900 truncate">{name}</p>
                    <a
                    href={`mailto:${email}`}
                    className="inline-flex items-center gap-1.5 text-sm text-slate-500 hover:text-teal-600 transition-colors"
                    >
                        <Mail className="h-3.5 w-3.5" />
                        <span className="truncate">{email}</span>
                    </a>
                </div>
            </div>
        </>
    )
}
