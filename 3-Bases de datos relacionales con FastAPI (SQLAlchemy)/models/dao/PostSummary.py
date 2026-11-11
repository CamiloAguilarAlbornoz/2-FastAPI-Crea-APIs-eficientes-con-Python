from pydantic import BaseModel, ConfigDict

class PostSummary(BaseModel):
    
    id_post: int
    title: str
    
    model_config = ConfigDict(from_attributes = True)