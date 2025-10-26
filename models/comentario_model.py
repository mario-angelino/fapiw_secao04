# models/comentario_model.py
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
import sqlalchemy.orm as orm
from core.configs import settings
from models.blog_post_model import BlogPostModel


class ComentarioModel(settings.DBBaseModel):
    """Comentários das postagens do blog"""
    __tablename__ = 'comentarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(DateTime, default=datetime.now, index=True)
    autor = Column(String(255), nullable=False)
    texto = Column(String(255), nullable=False)

    id_post = Column(Integer, ForeignKey('blog_post.id'))
    blog_post: BlogPostModel = orm.relationship('BlogPostModel', lazy='joined')
