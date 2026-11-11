from typing import List, Optional

from pydantic import BaseModel

from models.dao.PostPublic import PostPublic

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