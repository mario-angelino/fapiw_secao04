from datetime import datetime
from starlette.routing import Route
from fastapi.routing import APIRouter
from fastapi import status
from fastapi.requests import Request
from fastapi.responses import Response, RedirectResponse
from fastapi.exceptions import HTTPException
from core.configs import settings
from controllers.membro_controller import MembroController
from views.admin.base_crud_view import BaseCrudView


class MembroAdmin(BaseCrudView):
    def __init__(self):
        self.router = APIRouter()
        self.router.routes.append(Route(
            path='/membro/list', endpoint=self.object_list, methods=['GET',], name='membro_list'))
        self.router.routes.append(Route(
            path='/membro/create', endpoint=self.object_create, methods=['GET', 'POST'], name='membro_create'))
        self.router.routes.append(Route(
            path='/membro/details/{id_membro:int}', endpoint=self.object_edit, methods=['GET',], name='membro_details'))
        self.router.routes.append(Route(
            path='/membro/edit/{id_membro:int}', endpoint=self.object_edit, methods=['GET', 'POST'], name='membro_edit'))
        self.router.routes.append(Route(
            path='/membro/delete/{id_membro:int}', endpoint=self.object_delete, methods=['DELETE',], name='membro_delete'))
        super().__init__('membro')

    async def object_list(self, request: Request) -> Response:
        """
        Rota para listar todos os membros [GET]
        """
        membro_controller: MembroController = MembroController(request)
        return await super().object_list(object_controller=membro_controller)

    async def object_create(self, request: Request) -> Response:
        """
        Rota para carregar o template do formulário e criar um objeto [GET, POST]
        """
        membro_controller: MembroController = MembroController(request)

        # Se o request for GET
        if request.method == 'GET':
            # Adicionar o request no context
            context = {"request": membro_controller.request,
                       "ano": datetime.now().year}
            # Retorna o formulário de criação de membro
            return settings.TEMPLATES.TemplateResponse(f"admin/membro/create.html", context=context)

        # Se o request for POST
        form = await request.form()
        dados: set = None

        try:
            await membro_controller.post_crud()
        except ValueError as err:
            nome: str = form.get('nome')
            funcao: str = form.get('funcao')
            dados = {"nome": nome, "funcao": funcao}
            context = {
                "request": request,
                "ano": datetime.now().year,
                "error": err,
                "objeto": dados
            }
            return settings.TEMPLATES.TemplateResponse(f"admin/membro/create.html", context=context)

        # Se deu tudo certo, envia para lista de membros
        return RedirectResponse(request.url_for("membro_list"), status_code=status.HTTP_302_FOUND)

    async def object_edit(self, request: Request) -> Response:
        """
        Rota para carregar o template do formulário de edição e atualizar um objeto [GET, POST]
        """
        membro_controller: MembroController = MembroController(request)
        id_membro: int = request.path_params['id_membro']

        # Se o request for GET
        if request.method == 'GET':
            return await super().object_details(object_controller=membro_controller, id_obj=id_membro)

        # Se o request for POST
        membro = await membro_controller.get_one_crud(id_obj=id_membro)
        if not membro:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        form = await request.form()
        dados: set = None

        try:
            await membro_controller.put_crud(obj=membro)
        except ValueError as err:
            nome: str = form.get('nome')
            funcao: str = form.get('funcao')
            dados = {"id": id_membro, "nome": nome, "funcao": funcao}
            context = {
                "request": request,
                "ano": datetime.now().year,
                "error": err,
                "objeto": dados
            }
            return settings.TEMPLATES.TemplateResponse(f"admin/membro/edit.html", context=context)

        # Se deu tudo certo, envia para lista de membros
        return RedirectResponse(request.url_for("membro_list"), status_code=status.HTTP_302_FOUND)

    async def object_delete(self, request: Request) -> Response:
        """
        Rota para deletar um membro [DELETE]
        """
        membro_controller: MembroController = MembroController(request)
        id_membro: int = request.path_params['id_membro']
        return await super().object_delete(object_controller=membro_controller, id_obj=id_membro)


membro_admin = MembroAdmin()
