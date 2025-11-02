# models/membro_model.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
from core.configs import settings


class MembroModel(settings.DBBaseModel):
    __tablename__: str = 'membros'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(255))
    funcao: str = Column(String(100))
    imagem: str = Column(String(255))

    @validates('nome')
    def valida_funcao(self, key, value):
        if value is None or value == '':
            raise ValueError('Você precisa informar um nome válido.')
        return value

    @validates('funcao')
    def valida_funcao(self, key, value):
        if value is None or value == '':
            raise ValueError('Você precisa informar uma função válida.')
        return value
