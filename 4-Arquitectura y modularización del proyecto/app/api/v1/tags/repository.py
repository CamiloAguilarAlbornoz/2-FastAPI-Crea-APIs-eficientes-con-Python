from typing import List

from requests import Session
from sqlalchemy import func, select
from sqlalchemy.orm import joinedload
from app.models import TagORM
from app.models.post import PostORM

class TagRepository:
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_quantity_tags(self) -> List[TagORM]:
        count_tags = (
            select(TagORM)
            .options(
                joinedload(TagORM.posts)
            )
            .order_by(TagORM.name_tag)
        )
        return self.db.execute(count_tags).scalars().unique().all()