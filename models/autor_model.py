# models/autor_model.py
from typing import List, Optional
from sqlalchemy import Column, Integer, String, Table, ForeignKey
import sqlalchemy.orm as orm
from core.configs import settings
from models.tag_model import TagModel


# Autor pode ter várias tags
tags_autor = Table(
    'tags_autor',
    settings.DBBaseModel.metadata,
    Column('id_autor', Integer, ForeignKey('autores.id')),
    Column('id_tag', Integer, ForeignKey('tags.id'))
)


class AutorModel(settings.DBBaseModel):
    """Autor das postagens do blog"""
    __tablename__ = 'autores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    foto_url = Column(String(255))

    # Autor pode ter nenhuma ou várias tags
    tags: Optional[List[TagModel]] = orm.relationship(
        'TagModel', secondary=tags_autor, backref='taga', lazy='joined')
