from datetime import datetime
from fastapi import status
from fastapi.responses import Response
from fastapi.exceptions import HTTPException
from core.configs import settings


class BaseCrudView():

    def __init__(self, template_base: str) -> None:
        self.template_base: str = template_base

    async def object_create(self) -> Response:
        """
        Rota para carregar o template do formulário e criar um objeto [GET, POST]
        """
        raise NotImplementedError('Você precisa implementar este método.')

    async def object_edit(self) -> Response:
        """
        Rota para carregar o template do formulário de edição e atualizar um objeto [GET, POST]
        """
        raise NotImplementedError('Você precisa implementar este método.')
