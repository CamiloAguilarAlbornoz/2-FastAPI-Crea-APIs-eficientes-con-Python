from typing import List

from pydantic import BaseModel, ConfigDict


class TagQuantity(BaseModel):
    
    count: int
    tag_name: str
    model_config = ConfigDict(from_attributes = True)