from math import ceil
from typing import List, Literal, Optional, Union

from fastapi import APIRouter, Depends, HTTPException, Path, Query, status

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from app.core.db import get_db
from .schemas import PostPublic, PaginatedPost, PostCreate, PostUpdate, PostSummary
from .repository import PostRepository

router = APIRouter(prefix = '/posts', tags = ['posts'])

# Obtiene todos los post
@router.get('', response_model = PaginatedPost, response_model_exclude_none = True)
def posts(
    text: Optional[str] = Query(
        default = None,
        description = 'Buscar por título - Parametro obsoleto, usa query o search en su lugar',
        deprecated = True # Indica que este query o parametro está obsoleto
    ),
    query: Optional[str] = Query(
        default = None,
        description = 'Buscar por título',
        alias = 'search',
        min_length = 3,
        max_length = 50,
        pattern = r'^[\w\sáéíóúÁÉÍÓÚüÜ-]+$' # Expresión regular para que acepte tildes o ¨
    ),
    per_page: int = Query(10, ge = 1, le = 50, description = 'Número de resultados (1 - 50)'), # Cantidad de elementos por págima, 10 por defecto
    page: int = Query(1, ge = 1, description = 'Número de página >= 1'),
    order_by: Literal['id', 'title'] = Query('id', description = 'Campo de orden'),# Indica que solo se puede ingresar a los valores id y title
    direction: Literal['asc', 'desc'] = Query('asc', description = 'Dirección de orden'), # Indica que se pueden ordenar ascendente o descendente
    db: Session = Depends(get_db)
):
    repository = PostRepository(db)
    query = query or text
    total, items = repository.search(query, order_by, direction, page, per_page)
    total_pages = ceil(total / per_page) if total > 0 else 0
    current_page = min(page, total_pages) if total_pages != 0 else 1
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

# Filtra los post por sus tags
@router.get('/by-tags', response_model = List[PostPublic], response_model_exclude_none = True)
def filter_by_tags(
    tags: List[str] = Query(
        ...,
        min_length = 1,
        description = 'Una o más etiquetas, ejemplo: ?tags=python&tags=fastapi'
    ),
    db: Session = Depends(get_db)
):
    repository = PostRepository(db)
    return repository.by_tags(tags)

# Obtiene un post por su id
@router.get(
    '/{post_id}',
    response_model = Union[PostPublic, PostSummary],
    response_description = 'Post encontrado',
    response_model_exclude_none = True
)
def get_by_id(post_id: int = Path(
        ..., # Indica que si o si debe haber un parámetro
        ge = 1, # Indica que post_id deberá ser mayor o igual a 1
        title = 'ID del Post',
        description = 'Identificador entero del post, debe ser mayor a 1',
        example = 1),
    includes_content: bool = Query(default = True, description = 'Indica si incluye o no el contenido'),
    db: Session = Depends(get_db)):
    repository = PostRepository(db)
    post = repository.get(post_id)
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f'Post no encontrado')
    return PostPublic.model_validate(post, from_attributes = True) if includes_content else PostSummary.model_validate(post, from_attributes = True)

# Crea un nuevo post
@router.post(
    '',
    response_model = PostPublic,
    response_model_exclude_none = True,
    status_code = status.HTTP_201_CREATED
)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    repository = PostRepository(db)
    try:
        new_post = repository.create_post(
            title=post.title,
            content = post.content,
            author = post.author.model_dump() if post.author else None, # model_dump combierte el objeto a diccionario
            tags = [tag.model_dump() for tag in post.tags]) # Itera todos los tags y cada tag lo convierte en diccionario
        db.commit() # Confirma la operación
        db.refresh(new_post) # Actualiza la base de datos con la modificación
        return new_post
    except IntegrityError:
        db.rollback() # Si algo salio mal deshace el cambio
        raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail = 'El título ya existe, prueba con otro')
    except SQLAlchemyError:
        db.rollback() # Si algo salio mal deshace el cambio
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail = 'Error al crear el post')

# Actualiza un post
@router.put(
    '/{post_id}',
    response_model = PostPublic,
    response_model_exclude_none = True,
    status_code = status.HTTP_201_CREATED
)
def update_post(post_id: int, data: PostUpdate, db: Session = Depends(get_db)):
    repository = PostRepository(db)
    post = repository.get(post_id)
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'Post no encontrado')
    try:
        updates = data.model_dump(exclude_unset = True) # Se excluyen los campos que no se envíen
        post = repository.update_post(post, updates)
        db.commit()
        db.refresh(post)
        return post
    except SQLAlchemyError:
        db.rollback() # Si algo salio mal deshace el cambio
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail = 'Error al crear el post')

# Elimina un post
@router.delete(
    '/{post_id}',
    response_model_exclude_none = True,
    status_code = status.HTTP_204_NO_CONTENT
)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    repository = PostRepository(db)
    post = repository.get(post_id)
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'Post no encontrado')
    try:
        repository.delete_post(post)
        db.commit()
    except SQLAlchemyError:
        db.rollback() # Si algo salio mal deshace el cambio
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail = 'Error al crear el post')