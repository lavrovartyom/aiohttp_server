from aiohttp import web
from sqlalchemy.exc import IntegrityError
from models import User
from db import session
from aiohttp_pydantic import PydanticView
import schemas
from typing import List
from aiohttp_pydantic.oas.typing import r200, r201, r204


routes = web.RouteTableDef()


@routes.view('/')
class UserView(PydanticView):

    async def get(self) -> r200[List[schemas.UserOut]]:
        """
        Метод для получения все пользователей
        """
        users = session.query(User).all()
        result = [schemas.UserOut.from_orm(user).dict() for user in users]
        return web.json_response(result)

    async def post(self, user: schemas.UserIn) -> r201[schemas.UserOut]:
        """
        Метод для создания нового пользователя
        """
        new_user = User(**user.dict())
        try:
            with session.begin():
                session.add(new_user)
        except IntegrityError:
            return web.json_response('Ошибка! Такой пользователь уже есть!')
        return web.json_response(new_user.serialize)

    async def delete(self, id: int, /):
        """
        Метод для удаления пользователя
        """
        pass
