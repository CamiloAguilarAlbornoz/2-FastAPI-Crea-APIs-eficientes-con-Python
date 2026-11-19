import { useState, useRef, type KeyboardEvent } from "react";
import { useForm, useWatch } from 'react-hook-form'

import {
  Save,
  RotateCcw,
} from "lucide-react";
import type { Post } from "../../interfaces/post.interface";
import { CustomTitlePost } from "./CustomTitlePost";
import { CustomContentPost } from "./CustomContentPost";
import { CustomAuthorsPost } from "./CustomAuthorsPost";
import { CustomTagsPost } from "./CustomTagsPost";
import type { Tag } from "../../interfaces/tag.interface";

interface CreatePostPageProps {
    post?: Post,
    isPending: boolean,

    onCancel?: () => void;
    onSubmit: (postLike: Partial<Post>) => Promise<void>
}

export const CreateUpdatePostForm = ({ onCancel, onSubmit, post, isPending }: CreatePostPageProps) => {

    const [tags, setTags] = useState<string[]>([]);
    const [tagInput, setTagInput] = useState("");

    const tagInputRef = useRef<HTMLInputElement>(null);

    const{
        handleSubmit,
        register,
        formState: {errors},
        getValues, // Permite obtener los valores del formulario
        setValue, // Permite asignar valores al formulario
        control
    } = useForm({
        defaultValues: post
    })

    const tagsWatched = useWatch({
        control,
        name: 'tags'
    }) ?? [] // PERMITE ACTUALIZAR UN LISTADO APENAS TENGA UN CAMBIO

    const addTag = () => {
        if (tagInputRef.current === undefined || tagInputRef.current === null) return;
        const newTagName = tagInputRef.current.value || ''
        const newTag: Tag = {name_tag: newTagName.trim()}
        if ((newTag.name_tag.trim() && !tagsWatched.some(tag => tag.name_tag === newTagName))) {
            const tagSet = new Set(getValues('tags'))
            tagSet.add(newTag)
            setValue('tags', Array.from(tagSet))
        }
        tagInputRef.current.value = ''
    }

    const removeTag = (tag: string) => {
        setTags((prev) => prev.filter((t) => t !== tag));
    };

    const handleTagKeyDown = (e: KeyboardEvent<HTMLInputElement>) => {
        if (e.key === "Enter" || e.key === ",") {
            e.preventDefault();
            addTag();
        }
        else if (e.key === "Backspace" && tagInput === "" && tags.length > 0) {
            removeTag(tags[tags.length - 1]);
        }
    };

    const handleCancel = () => {
        setTags([]);
        setTagInput("");
        onCancel?.();
    };

    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <div className="overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm">
                <div className="space-y-7 p-6 sm:p-8">
                    {/* Title */}
                    <CustomTitlePost key = {post?.id_post} register = {register} errors = {errors}/>

                    {/* Content */}
                    <CustomContentPost
                    key = {post?.id_post}
                    register = {register}
                    errors = {errors}
                    post = {post} />

                    {/* Tags */}
                    <CustomTagsPost
                    handleTagKeyDown = {handleTagKeyDown}
                    tagInputRef = {tagInputRef}
                    tags = {tagsWatched || post?.tags || []}
                    removeTag = {removeTag}/>

                    {/* Authors */}
                    <CustomAuthorsPost key = {post?.id_post} register = {register} />
                </div>

                {/* Buttons */}
                <div className="flex items-center justify-end gap-3 border-t border-slate-200 bg-slate-50 px-6 py-4 sm:px-8">
                    <button
                    type="button"
                    onClick={handleCancel}
                    className="inline-flex items-center gap-2 rounded-lg px-4 py-2.5 text-sm font-semibold text-slate-700 transition-colors hover:bg-slate-200 active:bg-slate-300"
                    >
                        <RotateCcw className="h-4 w-4" />
                        Cancelar
                        </button>
                    <button
                    type="submit"
                    disabled = {isPending}
                    className="inline-flex items-center gap-2 rounded-lg bg-blue-600 px-4 py-2.5 text-sm font-semibold text-white shadow-sm transition-colors hover:bg-blue-700 active:bg-blue-800"
                    >
                        <Save className="h-4 w-4" />
                        Agregar
                    </button>
                </div>
            </div>
        </form>
    )
}
