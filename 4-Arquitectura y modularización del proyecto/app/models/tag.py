from typing import List, TYPE_CHECKING

from app.core.db import Base

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .post import PostORM

class TagORM(Base):
    
    __tablename__ = 'tags'
    id_tag: Mapped[int] = mapped_column(Integer, primary_key = True, index = True)
    name_tag: Mapped[int] = mapped_column(String(30), index = True)
    
    posts: Mapped[List['PostORM']] = relationship(
        secondary = 'post_tags',
        back_populates = 'tags',
        lazy = 'selectin'
    )