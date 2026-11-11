from typing import List

from sqlalchemy import Integer, String

from models.entities.Base import Base
from models.entities.Post_Tags import post_tags

from sqlalchemy.orm import Mapped, mapped_column, relationship

class TagORM(Base):
    
    __tablename__ = 'tags'
    id_tag: Mapped[int] = mapped_column(Integer, primary_key = True, index = True)
    name_tag: Mapped[int] = mapped_column(String(30), index = True)
    
    posts: Mapped[List['PostORM']] = relationship( # type: ignore
        secondary = post_tags,
        back_populates = 'tags',
        lazy = 'selectin'
    )