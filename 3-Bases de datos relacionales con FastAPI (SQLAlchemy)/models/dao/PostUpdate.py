from typing import Optional

from pydantic import BaseModel, Field


class PostUpdate(BaseModel):
    
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    content: Optional[str] = None # Indica que el content es opcional, se usa None para que en caso de una actualización se conserve lo que ya se tenía