from models.dao.PostUpdate import PostUpdate
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.entities.PostORM import PostORM

def update_post_service(post_id: int, data: PostUpdate, db: Session):
    post = db.get(PostORM, post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post no encontrado')
    updates = data.model_dump(exclude_unset = True) # exclude_unset es para que en la respuesta no aparezca null en campos vacíos
    for key, value in updates.items():
        post.__setattr__(key, value)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post