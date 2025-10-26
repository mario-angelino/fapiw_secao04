# models/blog_post_model.py
from typing import List, Optional
from datetime import datetime
import sqlalchemy.orm as orm
from sqlalchemy import Column, Integer, String, DateTime, Table, ForeignKey
from core.configs import settings
from models.tag_model import TagModel
from models.autor_model import AutorModel
from models.comentario_model import ComentarioModel

# Blog_post pode ter várias tags
tags_post = Table(
    'tags_post',
    settings.DBBaseModel.metadata,
    Column('id_blog_post', Integer, ForeignKey('blog_post.id')),
    Column('id_tag', Integer, ForeignKey('tags.id'))
)

# Blog_post pode ter vários comentários
comentarios_post = Table(
    'comentarios_post',
    settings.DBBaseModel.metadata,
    Column('id_blog_post', Integer, ForeignKey('blog_post.id')),
    Column('id_comentario', Integer, ForeignKey('comentarios.id'))
)


class BlogPostModel(settings.DBBaseModel):
    """Posts do blog"""
    __tablename__ = 'blog_post'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(255), nullable=False)
    data = Column(DateTime, default=datetime.now, index=True)
    foto_url = Column(String(255))
    texto = Column(String(1000), nullable=False)

    id_autor = Column(Integer, ForeignKey('autores.id'))
    autor: AutorModel = orm.relationship('AutorModel', lazy='joined')

    # Um post pode ter várias tags
    tags: List[TagModel] = orm.relationship(
        'TagModel', secondary='tags_post', backref='tagp', lazy='joined')

    # Um post pode ter vários comentários
    comentarios: Optional[List[ComentarioModel]] = orm.relationship(
        'ComentarioModel', secondary='comentarios_post', backref='comentariop', lazy='joined')
