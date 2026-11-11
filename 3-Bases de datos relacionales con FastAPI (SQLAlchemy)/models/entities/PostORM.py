from datetime import datetime, timezone
from typing import List, Optional

from sqlalchemy import DateTime, Integer, String, Text, UniqueConstraint, ForeignKey

from models.entities.Post_Tags import post_tags
from models.entities.Base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class PostORM(Base):
    
    __tablename__ = 'posts' # Tabla posts
    __table_args__ = (UniqueConstraint('title', name='unique_post_title'),) # indica que el title será un campo unico
    
    id_post: Mapped[int] = mapped_column(Integer, primary_key = True, index = True) # Columna id del post
    title: Mapped[str] = mapped_column(String(100), nullable = False, index = True) # Columna del título
    content: Mapped[str] = mapped_column(Text, nullable = True) # Columna del contenido
    create_at: Mapped[datetime] = mapped_column(DateTime(timezone = True), default = lambda: datetime.now(timezone.utc))
    
    author_id: Mapped[Optional[int]] = mapped_column(ForeignKey('authors.id_author')) # llave foranea relacionada al id de tabla autores
    author: Mapped[Optional['AuthorORM']] = relationship(back_populates = 'posts') # type: ignore # Author al que pertenece el post
    
    tags: Mapped[List['TagORM']] = relationship( # type: ignore
        secondary = post_tags, # Se establece que la relación entre Post y Tag será a través de la tabla intermedia post_tags
        back_populates = 'posts', # Los tags podrán acceder a los post por medio de posts 
        lazy = 'selectin', # La busqueda la hace con selectin
        passive_deletes = True # respeta el ondelete en cascada
    )