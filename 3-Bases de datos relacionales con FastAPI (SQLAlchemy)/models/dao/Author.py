from pydantic import BaseModel, ConfigDict, EmailStr, Field


class Author(BaseModel):
    
    name: str = Field(..., min_length=5, max_length=30, description='Nombre del autor', 
                    validation_alias='name_author',)
    email: EmailStr  = Field(..., min_length=10, max_length=30, description='Email del autor',
                    validation_alias='email_author',)
    model_config = ConfigDict(from_attributes = True)