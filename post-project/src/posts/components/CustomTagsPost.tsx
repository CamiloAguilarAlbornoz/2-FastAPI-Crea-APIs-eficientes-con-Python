import { TagIcon, X } from "lucide-react";
import type { KeyboardEvent, RefObject } from "react";
import type { Tag } from "../../interfaces/tag.interface";

interface Props {
    tags: Tag[],
    tagInputRef: RefObject<HTMLInputElement | null>,

    removeTag: (tag: string) => void,
    handleTagKeyDown: (e: KeyboardEvent<HTMLInputElement>) => void
}

export const CustomTagsPost = ({tags, tagInputRef, removeTag, handleTagKeyDown}: Props) => {

    return (
        <div>
            <label
                htmlFor="tags"
                className="mb-1.5 flex items-center gap-2 text-sm font-semibold text-slate-800"
            >
                <TagIcon className="h-4 w-4 text-blue-600" />
                Etiquetas
            </label>
            <div
                onClick={() => tagInputRef.current?.focus()}
                className={`flex flex-wrap items-center gap-2 rounded-lg border px-2.5 py-2 transition-colors ${
                tags.length > 0
                    ? "border-slate-300 focus-within:border-blue-500 focus-within:ring-2 focus-within:ring-inset focus-within:ring-blue-200"
                    : "border-slate-300 focus-within:border-blue-500 focus-within:ring-2 focus-within:ring-inset focus-within:ring-blue-200"
                }`}
            >
                {tags.map((tag) => (
                <span
                    key={tag.name_tag}
                    className="inline-flex items-center gap-1 rounded-md bg-blue-50 px-2 py-1 text-xs font-medium text-blue-700"
                >
                    {tag.name_tag}
                    <button
                    type="button"
                    onClick={(e) => {
                        e.stopPropagation();
                        removeTag(tag.name_tag);
                    }}
                    className="text-blue-400 transition-colors hover:text-blue-700"
                    >
                    <X className="h-3 w-3" />
                    </button>
                </span>
                ))}
                <input
                ref={tagInputRef}
                id="tags"
                type="text"
                onKeyDown={handleTagKeyDown}
                placeholder={
                    tags.length === 0
                    ? "Escribe una etiqueta y presiona Enter..."
                    : "Agregar otra..."
                }
                className="flex-1 min-w-37.5 border-0 bg-transparent py-1 text-sm text-slate-900 placeholder-slate-400 outline-none"
                />
            </div>
            <p className="mt-1.5 text-xs text-slate-400">
                Presiona Enter o coma para agregar. {tags.length} etiqueta
                {tags.length === 1 ? "" : "s"}.
            </p>
        </div>
    )
}
