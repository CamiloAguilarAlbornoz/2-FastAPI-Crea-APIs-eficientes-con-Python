from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.entities.PostORM import PostORM

def delete_post_service(post_id: int, db: Session):
    post = db.get(PostORM, post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Post no encontrado')
    db.delete(post)
    db.commit()
    return post