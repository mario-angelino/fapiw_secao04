# models/tag_model.py
from sqlalchemy import Column, Integer, String
from core.configs import settings


class TagModel(settings.DBBaseModel):
    """Temos tags em várias partes do website"""
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tag = Column(String(255), nullable=False)
