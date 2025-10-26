# models/area_model.py
from sqlalchemy import Column, Integer, String
from core.configs import settings


class AreaModel(settings.DBBaseModel):
    """Dúvidas respondidas no FAQ são categorizadas em áreas"""
    __tablename__ = 'areas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    area = Column(String(255), nullable=False)
