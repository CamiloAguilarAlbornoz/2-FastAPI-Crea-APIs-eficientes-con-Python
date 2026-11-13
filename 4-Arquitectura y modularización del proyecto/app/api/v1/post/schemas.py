from typing import List, Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


class Author(BaseModel):
    
    name: str = Field(..., min_length=5, max_length=30, description='Nombre del autor', 
                    validation_alias='name_author',)
    email: EmailStr  = Field(..., min_length=10, max_length=30, description='Email del autor',
                    validation_alias='email_author',)
    model_config = ConfigDict(from_attributes = True)

class Tag(BaseModel):
    
    name: str = Field(..., min_length=2, max_length=30, description='Nombre de la etiqueta', validation_alias='name_tag',)
    model_config = ConfigDict(from_attributes = True) # Para que acepte objetos ORM

class PostBase(BaseModel):
    
    title: str
    content: str
    tags: Optional[List[Tag]] = Field(default_factory = list) # Crea una lista vacía, creando una por cada objeto que se crea en el programa
    author: Optional[Author] = None
    model_config = ConfigDict(from_attributes = True)

class PostPublic(PostBase):
    
    id_post: int
    model_config = ConfigDict(from_attributes = True) # Sirve para que esta clase se valide a partir de un objeto

class PaginatedPost(BaseModel):
    
    page: int
    per_page: int
    total: int
    total_pages: int
    has_prev: bool
    has_next: bool
    order_by: str
    direction: str
    search: Optional[str]
    items: List[PostPublic]

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

class PostSummary(BaseModel):
    
    id_post: int
    title: str
    
    model_config = ConfigDict(from_attributes = True)

class PostUpdate(BaseModel):
    
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    content: Optional[str] = None # Indica que el content es opcional, se usa None para que en caso de una actualización se conserve lo que ya se tenía