from pydantic import BaseModel, ConfigDict, Field


class Tag(BaseModel):
    
    name: str = Field(..., min_length=2, max_length=30, description='Nombre de la etiqueta', validation_alias='name_tag',)
    model_config = ConfigDict(from_attributes = True) # Para que acepte objetos ORM