# models/faq_models.py
import sqlalchemy.orm as orm
from sqlalchemy import Column, Integer, String, ForeignKey
from core.configs import settings
from models.area_model import AreaModel


class FaqModel(settings.DBBaseModel):
    __tablename__ = 'faq'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(255), nullable=False)
    resposta = Column(String(255), nullable=False)

    id_area = Column(Integer, ForeignKey('areas.id'))
    area: AreaModel = orm.relationship('AreaModel', lazy='joined')