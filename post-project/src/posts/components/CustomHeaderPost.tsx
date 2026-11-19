import { Tag as TagPeg } from "lucide-react";
import type { Tag } from "../../interfaces/tag.interface";

interface Props {
    title: string;
    tags?: Tag[]
}

export const CustomHeaderPost = ({title, tags}: Props) => {
    return (
        <>
            <header className="border-b border-slate-100 px-6 py-6 sm:px-10 sm:py-8">
                <h1 className="text-3xl sm:text-4xl font-bold text-slate-900 leading-tight">
                    {title}
                </h1>

                <div className="mt-6 flex flex-wrap gap-2">
                {
                    tags !== undefined && (
                        tags.map((tag) => (
                            <span
                            key={tag.name_tag}
                            className="inline-flex items-center gap-1.5 rounded-full bg-teal-50 border border-teal-200 px-3 py-1 text-sm font-medium text-teal-700 transition-colors hover:bg-teal-100"
                            >
                            <TagPeg className="h-3.5 w-3.5" />
                                {tag.name_tag}
                            </span>
                        ))
                    )
                }
                </div>
            </header>
        </>
    )
}
