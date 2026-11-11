from typing import List, Optional

from pydantic import BaseModel, Field, field_validator

from models.dao.Author import Author
from models.dao.Tag import Tag


class PostCreate(BaseModel):
    
    title: str = Field(
        ..., # Indica que el campo es obligatorio, elipsis
        min_length=3, # Indica que el campo debe tener un mínimo de 3 caracteres
        max_length=100, # Indica que el campo deberá tener máximo 100 caracteres
        description='Titulo del Post (mínimo 3 caracteres y máximo 100)', # Descripción del campo
        examples=['Mi primer post con fastAPI'] # Ejemplo que verá el usuario en la documentación
    )
    content: Optional[str] = Field(
        default='Contenido pendiente...', # Valor por defecto del campo
        min_length=10,
        description='Contenido del post (mínimo 10 caracteres)',
        examples=['Este es un contenido valido porque tiene 10 caracteres o más']
    )
    tags: List[Tag] = Field(default_factory = list)
    author: Optional[Author] = None
    
    '''
    Se encarga de evaluar el title de forma más avanzada
    '''
    @field_validator('title') # Evalua el campo que se ingrese por parametro, title en este caso
    @classmethod # Indica que se va a ocupar la clase completa, util para evaluarla completamente
    def not_allowed_title(cls, value: str) -> str:
        words_not_allowd = ['porn', 'xxx', 'count', 'pussy', 'cock', 'dick', 'spam']
        for word in words_not_allowd:
            if word in value.lower():
                raise ValueError(f'El título no puede contener la palabra {word}')
        return value