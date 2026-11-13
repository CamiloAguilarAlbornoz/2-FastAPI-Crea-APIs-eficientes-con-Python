from math import ceil
from typing import List, Optional, Tuple

from sqlalchemy import func, select
from sqlalchemy.orm import Session, joinedload, selectinload
from app.models import PostORM, TagORM, AuthorORM

class PostRepository:
    
    def __init__(self, db: Session):
        self.db = db
    
    # Obtiene un post por id
    def get(self, post_id: int) -> Optional[PostORM]:
        '''
        post_find = select(PostORM).where(post_id == PostORM.id_post)
        post = db.execute(post_find).scalar_one_or_none()
        '''
        return self.db.get(PostORM, post_id) # Se usa este para buscar un post con un primary key
    
    # Obtiene los post en una tupla
    def search(self, query: Optional[str], order_by: str, direction: str, page: int, per_page: int) -> Tuple[int, List[PostORM]]:
        results = select(PostORM)
        if query:
            results = results.where(PostORM.title.ilike(f'%{query}%')) # Filtra los resultados con base al query
        total = self.db.scalar(
            select(func.count())
            .select_from(results.subquery())) or 0 # Obtiene un conteo total de los registros filtrados
        if total == 0: return 0, []
        order_col = PostORM.id_post if order_by == 'id' else func.lower(PostORM.title) # Ordena los resultados por id o titulo
        results = results.order_by(
            order_col.asc() if direction == 'asc' else order_col.desc()) # Ordena ascendente o descendente según sea la dirección
        total_pages = ceil(total / per_page)
        current_page = min(page, max(1, total_pages))
        start = (current_page - 1) * per_page
        items = self.db.execute(
            results.limit(per_page) # Limita el número de resultados por página
            .offset(start) # Salta los registros de páginas anteriores para no repetir valores
            ).scalars().all() # Extrae los objetos de la entity y no la fila completa
        return total, items
    
    # Obtener post por tags
    def by_tags(self, tag_names: List[str]) -> List[PostORM]:
        normalized_tags_names = [tag.strip().lower() for tag in tag_names if tag.strip()]
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
        return self.db.execute(post_list).scalars().all() # Ejecuta la busqueta y el resultado lo guarda en posts
    
    # Busca un autor y si no existe lo crea con los datos que se le enviaron y lo agrega a la BD
    def ensure_author(self, name: str, email: str) -> AuthorORM:
        author_obj = self.db.execute(
            select(AuthorORM).where(AuthorORM.email_author == email)
        ).scalar_one_or_none() # Busca el autor en la base de datos
        if author_obj: return author_obj
        author_obj = AuthorORM(name_author = name, email_author = email) # Si no existe el autor, lo crea
        self.db.add(author_obj) # Lo agrega a la base de datos
        self.db.flush() # Asigna el ID, hay casos en que no es necesario si se hizo el commit
        return author_obj
    
    # Busca un tag y si no existe lo crea con los datos que se le enviaron y lo agrega a la BD
    def ensure_tag(self, name: str) -> TagORM:
        tag_obj = self.db.execute(
                        select(TagORM).where(TagORM.name_tag.ilike(name))
                    ).scalar_one_or_none()
        if tag_obj: return tag_obj
        tag_obj = TagORM(name_tag = name)
        self.db.add(tag_obj)
        self.db.flush()
        return tag_obj
    
    # Crea un post
    def create_post(self, title: str, content: str, author: Optional[dict], tags: List[dict]) -> PostORM:
        author_obj = None
        if author:
            author_obj = self.ensure_author(author['name'], author['email'])
        #post = PostORM(title, content, author = author_obj)
        post = PostORM(title = title, content = content, author = author_obj)
        for tag in tags:
            tag_object = self.ensure_tag(tag['name'])
            post.tags.append(tag_object)
        self.db.add(post) # Agrega el Post
        self.db.flush()
        return post
    
    # Actualiza un post
    def update_post(self, post: PostORM, updates: dict) -> PostORM:
        for key, value in updates.items():
            post.__setattr__(key, value)
        self.db.add(post)
        return post
    
    # Elimina un post
    def delete_post(self, post: PostORM) -> None:
        self.db.delete(post)