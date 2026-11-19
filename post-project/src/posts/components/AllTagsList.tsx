import { useTags } from "../hooks/useTags";

const TAG_COLORS = [
  'bg-sky-100 text-sky-700 border-sky-200 hover:bg-sky-200',
  'bg-emerald-100 text-emerald-700 border-emerald-200 hover:bg-emerald-200',
  'bg-amber-100 text-amber-700 border-amber-200 hover:bg-amber-200',
  'bg-rose-100 text-rose-700 border-rose-200 hover:bg-rose-200',
  'bg-violet-100 text-violet-700 border-violet-200 hover:bg-violet-200',
];

const SELECTED_TAG_CLASS = 'bg-sky-600 text-white border-sky-600 hover:bg-sky-700';

const tagColor = (tag: string) => {
  let hash = 0;
  for (let i = 0; i < tag.length; i++) {
    hash = (hash * 31 + tag.charCodeAt(i)) % 997;
  }
  return TAG_COLORS[hash % TAG_COLORS.length];
}

export const AllTagsList = () => {
    
  const{
    tags,
    firtsTags,
    toggleTag
  } = useTags()

  return (
      <>
        <aside className="lg:w-60 lg:shrink-0">
          <div className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm lg:sticky lg:top-24">
            <h2 className="text-sm font-semibold uppercase tracking-wide text-slate-500">
              Etiquetas
            </h2>
            <div className="mt-4 flex flex-wrap gap-2">
              {
                tags !== undefined && (
                  tags.map(tag => {
                    const isSelected = firtsTags.includes(tag.tag_name);
                    return (
                      <button
                      key={tag.tag_name}
                      onClick={() => toggleTag(tag.tag_name)}
                      aria-pressed={isSelected}
                      className={`inline-flex items-center gap-1.5 rounded-full border px-3 py-1 text-xs font-medium transition-colors ${
                        isSelected ? SELECTED_TAG_CLASS: tagColor(tag.tag_name)}`
                      }
                      >
                        {tag.tag_name}
                        <span className="opacity-60">{tag.count}</span>
                      </button>
                    )
                  } )
                )
              }
            </div>
          </div>
        </aside>
      </>
  )
}
