from typing import List

from fastapi import APIRouter, Depends
from requests import Session

from app.api.v1.tags.repository import TagRepository
from app.api.v1.tags.schemas import TagQuantity
from app.core.db import get_db

router = APIRouter(prefix = '/tags', tags = ['tags'])
@router.get('/count', response_model = List[TagQuantity])
def count_tags_by_post(db: Session = Depends(get_db)):
    repository = TagRepository(db)
    tags = repository.get_quantity_tags()
    tags_quantity: List[TagQuantity] = []
    for tag in tags:
        count = len(tag.posts)
        if count > 0:
            tags_quantity.append(TagQuantity(count = len(tag.posts), tag_name = tag.name_tag))
    return tags_quantity