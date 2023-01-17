from aiohttp import web
from sqlalchemy.exc import IntegrityError
from models import User
from db import session
from aiohttp_pydantic import PydanticView
import schemas
from typing import List
from aiohttp_pydantic.oas.typing import r200, r201


routes = web.RouteTableDef()


@routes.view('/')
class UserView(PydanticView):

    async def get(self, /) -> r200[List[schemas.UserOut]]:
        """
        Метод для получения все пользователей
        :return: json response
        """
        users = session.query(User).all()
        result = [schemas.UserOut.from_orm(user).dict() for user in users]
        return web.json_response(result, status=200)

    async def post(self, user: schemas.UserIn) -> r201[schemas.UserOut]:
        """
        Метод для создания нового пользователя
        :param user: данные о пользователе
        :return: json response
        """
        new_user = User(**user.dict())
        try:
            with session.begin():
                session.add(new_user)
        except IntegrityError:
            return web.json_response('Ошибка! Такой пользователь уже есть!')
        return web.json_response(user.dict(), status=201)

    async def delete(self, id: int) -> r200:
        """
        Метод для удаления пользователя по id
        :param id: идентификатор пользователя
        :return: json response
        """
        session.query(User).filter(User.id == id).delete()
        return web.json_response(text='Объект успешно удален!', status=200)

    async def patch(self, id: int):
        """
        Метод для обновления данных о пользователе
        :return: json response
        """
        data: dict = await self.request.json()

        return web.json_response()

