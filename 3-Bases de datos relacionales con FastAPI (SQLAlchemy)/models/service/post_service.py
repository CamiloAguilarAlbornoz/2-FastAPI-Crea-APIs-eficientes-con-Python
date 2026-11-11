from fastapi import HTTPException, status
from sqlalchemy import select

from models.dao.PostCreate import PostCreate
from models.entities.AuthorORM import AuthorORM
from models.entities.PostORM import PostORM
from models.entities.TagORM import TagORM

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

def create_post_service(post: PostCreate, db: Session):
    # Obtiene o crea el autor
    author_obj = None
    if post.author:
        author_obj = db.execute(
            select(AuthorORM).where(AuthorORM.email_author == post.author.email)
        ).scalar_one_or_none() # Si llegó un autor por el api, busca en la base de datos ese autor
        if not author_obj:
            author_obj = AuthorORM(name_author = post.author.name, email_author = post.author.email)
            db.add(author_obj)
            db.flush() # Asigna el ID, hay casos en que no es necesario si se hizo el commit
    
    # Crea el Post y lo agrega a la BD
    new_post = PostORM(title = post.title, content = post.content, author = author_obj)
    
    # Obtiene o crea los tags
    for tag in post.tags:
        tag_obj = db.execute(
            select(TagORM).where(TagORM.name_tag.ilike(tag.name))
        ).scalar_one_or_none()
        if not tag_obj:
            tag_obj = TagORM(name_tag = tag.name)
            db.add(tag_obj)
            db.flush()
        new_post.tags.append(tag_obj) # Agrega el tag a la tabla intermedia
    try:
        db.add(new_post) # Agrega el Post
        db.commit() # Confirma la operación
        db.refresh(new_post) # Actualiza la base de datos con la modificación
        return new_post
    except IntegrityError:
        db.rollback() # Si algo salio mal deshace el cambio
        raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail = 'El título ya existe, prueba con otro')
    except SQLAlchemyError:
        db.rollback() # Si algo salio mal deshace el cambio
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail = 'Error al crear el post')