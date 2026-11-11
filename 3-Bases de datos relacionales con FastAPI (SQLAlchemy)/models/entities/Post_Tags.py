from sqlalchemy import Column, ForeignKey, Table

from models.entities.Base import Base


post_tags = Table(
    'post_tags',
    Base.metadata,
    Column('id_post_fk', ForeignKey('posts.id_post', ondelete = 'CASCADE'), primary_key = True),
    Column('if_tag_fk', ForeignKey('tags.id_tag', ondelete = 'CASCADE'), primary_key = True)
)