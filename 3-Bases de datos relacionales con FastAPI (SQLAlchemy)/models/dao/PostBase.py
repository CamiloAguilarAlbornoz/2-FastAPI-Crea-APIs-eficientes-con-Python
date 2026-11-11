from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field
from models.dao.Tag import Tag
from models.dao.Author import Author


class PostBase(BaseModel):
    
    title: str
    content: str
    tags: Optional[List[Tag]] = Field(default_factory = list) # Crea una lista vacía, creando una por cada objeto que se crea en el programa
    author: Optional[Author] = None
    model_config = ConfigDict(from_attributes = True)