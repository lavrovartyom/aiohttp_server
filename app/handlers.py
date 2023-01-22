from aiohttp import web
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
from models import User
from db import session
from aiohttp_pydantic import PydanticView
import schemas
from typing import List
from aiohttp_pydantic.oas.typing import r200, r201, r202
from logic import hash_password


routes = web.RouteTableDef()


@routes.view('/')
class UserView(PydanticView):

    async def get(self) -> r200[List[schemas.UserOut]]:
        """
        Метод для получения всеx пользователей
        :return: json response
        """
        users = session.query(User).all()
        result = [schemas.UserOut.from_orm(user).dict() for user in users]
        return web.json_response(result, content_type='application/json', status=200)

    async def post(self, user: schemas.UserIn) -> r201[schemas.UserOut]:
        """
        Метод для создания нового пользователя
        :param user: данные о пользователе
        :return: json response
        """
        new_user = User(**user.dict())
        new_user.password = hash_password(new_user.password)
        try:
            with session.begin():
                session.add(new_user)
        except IntegrityError:
            return web.json_response('Ошибка! Такой пользователь уже есть!')
        return web.json_response(user.dict(), content_type='application/json', status=201)

    async def delete(self, id: int) -> r202:
        """
        Метод для удаления пользователя по id
        :param id: идентификатор пользователя
        :return: json response
        """
        session.query(User).filter(User.id == id).delete()
        session.commit()
        return web.json_response(text='Объект успешно удален!', content_type='application/json', status=202)

    async def put(self, id: int, user: schemas.BaseUser) -> r200[schemas.UserOut]:
        """
        Метод для обновления всех данных о пользователе
        :return: json response
        """
        try:
            session.query(User).filter(User.id == id).update(
                {
                    User.first_name: user.first_name,
                    User.last_name: user.last_name,
                    User.login: user.login,
                    User.date_of_birth: user.date_of_birth,
                    User.permission: user.permission
                }
            )
            session.commit()
            return web.json_response({'Пользователь обновлен': user.dict()}, content_type='application/json', status=200)
        except (IntegrityError, UniqueViolation) as exc:
            web.json_response(text=f'{exc}', content_type='application/json')

    async def patch(self, id: int):
        pass


@routes.get('/user/{user_id}')
async def get_user(request) -> r200[List[schemas.UserOut]]:
    """
    Обработчик для получения пользователя по идентификатору
    """
    user = session.query(User).where(User.id == request.match_info['user_id']).one_or_none()
    if user:
        result = schemas.UserOut.from_orm(user).dict()
        return web.json_response(result, content_type='application/json', status=200)

    return web.json_response(text='Пользователь не найден', content_type='application/json', status=200)

