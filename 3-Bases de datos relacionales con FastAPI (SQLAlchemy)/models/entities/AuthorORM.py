from typing import List

from models.entities.Base import Base

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class AuthorORM(Base):
    __tablename__ = 'authors' # Tabla authors
    
    id_author: Mapped[int] = mapped_column(Integer, primary_key = True, index = True) # id del autor y llave primaria
    name_author: Mapped[str] = mapped_column(String(100), nullable = False) # nombre del autor
    email_author: Mapped[str] = mapped_column(String(), nullable = False) # correo del autor
    
    posts: Mapped[List['PostORM']] = relationship(back_populates = 'author') # type: ignore # Lista de posts de cada autor