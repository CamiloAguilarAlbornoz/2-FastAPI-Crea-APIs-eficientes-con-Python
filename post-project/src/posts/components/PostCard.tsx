import { useState } from "react";
import type { Post } from "../../interfaces/post.interface";
import { useNavigate } from "react-router";

const TRUNCATE_LENGTH = 180;

export const PostCard = ({ post }: { post: Post }) => {

  const [expanded, setExpanded] = useState(false);
  const isLong = post.content.length > TRUNCATE_LENGTH;

  const navegate = useNavigate()

  const handleClic = () => {
    navegate(`/post/${post.id_post}`)
  }

  return (
    <article 
    className = "flex flex-col rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-lg hover:border-sky-200"
    >
      <h3 className="text-lg font-semibold text-slate-900 leading-snug mb-3" onClick = {handleClic}>
        <a className="cursor-pointer">{post.title}</a>
      </h3>
      <p className="text-sm text-slate-600 leading-relaxed whitespace-pre-line flex-1">
        {expanded || !isLong ? post.content : `${post.content.slice(0, TRUNCATE_LENGTH)}…`}
      </p>
      {isLong && (
        <button
          onClick={() => setExpanded((prev) => !prev)}
          className="mt-4 self-start text-sm font-semibold text-sky-600 hover:text-sky-700 underline-offset-4 hover:underline transition-colors"
        >
          {expanded ? 'Ver menos' : 'Ver más'}
        </button>
      )}
    </article>
  );
}