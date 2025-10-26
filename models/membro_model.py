from sqlalchemy import Column, Integer, String
from core.configs import settings


class MembroModel(settings.DBBaseModel):
    __tablename__: str = 'membros'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(255))
    funcao: str = Column(String(100))
    foto_url: str = Column(String(255))
