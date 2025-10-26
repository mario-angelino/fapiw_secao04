# models/projeto_model.py
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from core.configs import settings


class ComentarioModel(settings.DBBaseModel):
    """No website temos um portfolio de projetos"""
    __tablename__ = 'projetos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(DateTime, default=datetime.now, index=True)
    titulo = Column(String(100), nullable=False)
    descricao_inicial = Column(String(255), nullable=False)
    descricao_final = Column(String(255))
    link = Column(String(255))
    imagem_01 = Column(String(255))
    imagem_02 = Column(String(255))
    imagem_03 = Column(String(255))
