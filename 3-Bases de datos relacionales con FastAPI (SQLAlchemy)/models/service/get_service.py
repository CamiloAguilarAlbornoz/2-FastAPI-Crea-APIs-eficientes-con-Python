from math import ceil
from typing import List, Literal, Optional

from fastapi import HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.orm import Session, selectinload, joinedload

from models.dao.PaginatedPost import PaginatedPost
from models.dao.PostPublic import PostPublic
from models.dao.PostSummary import PostSummary
from models.entities.PostORM import PostORM
from models.entities.TagORM import TagORM

def filter_by_tags_service(tags: List[str], db: Session):
    normalized_tags_names = [tag.strip().lower() for tag in tags if tag.strip()]
    if not normalized_tags_names:
        return []
    post_list = (
        select(PostORM)
        .options(
            selectinload(PostORM.tags), # Evitar el problema n + 1 al serializar, serializa la llamada a los posttags
            joinedload(PostORM.author), # Trae el autor de los Post
        ).where(PostORM.tags.any(func.lower(TagORM.name_tag).in_(normalized_tags_names))) # Pregunta si en las tags de PostORM hay algun tag que este incluida en la lista normalized_tags_names o que tenga que ver con elementos de normalized_tags_names
        .order_by(PostORM.id_post.asc()) # Lo ordena ascendentemente por el ID
    )
    posts = db.execute(post_list).scalars().all() # Ejecuta la busqueta y el resultado lo guarda en posts
    return posts

def posts_service(text: Optional[str], query: Optional[str], per_page: int, page: int, 
                order_by: Literal['id', 'title'], direction: Literal['asc', 'desc'], db: Session):
    results = select(PostORM)
    
    if query: results = results.where(PostORM.title.ilike(f'%{query}%')) # Filtra los resultados con base al query
    
    total = db.scalar(
        select(func.count())
        .select_from(results.subquery())) or 0 # Obtiene un conteo total de los registros filtrados
    
    if order_by == 'id':
        order_col = PostORM.id_post # Ordena los resultados por id
    else:
        order_col = func.lower(PostORM.title) # Ordena los resultados por titulo
    
    results = results.order_by(
        order_col.asc() if direction == 'asc' else order_col.desc()) # Ordena ascendente o descendente según sea la dirección
    
    total_pages = ceil(total / per_page) if total > 0 else 0
    
    current_page = min(page, total_pages) if total_pages != 0 else 1
    
    if total_pages == 0:
        items = List[PostORM]
    else:
        start = (current_page - 1) * per_page
        items = db.execute(
            results.limit(per_page) # Limita el número de resultados por página
            .offset(start) # Salta los registros de páginas anteriores para no repetir valores
            ).scalars().all() # Extrae los objetos de la entity y no la fila completa
    
    has_prev = page != 1
    has_next = page != total_pages
    
    return PaginatedPost(
        per_page = per_page,
        items = items,
        total = total,
        total_pages = total_pages,
        page = current_page,
        has_prev = has_prev,
        has_next = has_next,
        order_by = order_by,
        direction = direction,
        search = query
    )

def get_post_by_id_service(post_id: int, includes_content: bool, db: Session):
    '''
    post_find = select(PostORM).where(post_id == PostORM.id_post)
    post = db.execute(post_find).scalar_one_or_none()
    '''
    post = db.get(PostORM, post_id) # Se usa este para buscar un post con un primary key
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Post no encontrado')
    if includes_content:
        return PostPublic.model_validate(post, from_attributes = True)
    return PostSummary.model_validate(post, from_attributes = True)