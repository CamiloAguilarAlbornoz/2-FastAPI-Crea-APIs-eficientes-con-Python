from pydantic import ConfigDict

from models.dao.PostBase import PostBase

class PostPublic(PostBase):
    
    id_post: int
    model_config = ConfigDict(from_attributes = True) # Sirve para que esta clase se valide a partir de un objeto