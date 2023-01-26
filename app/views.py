from aiohttp import web
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
from models import User
from db import session
from aiohttp_pydantic import PydanticView
import schemas
from typing import List
from aiohttp_pydantic.oas.typing import r200, r201, r202
from passlib.hash import pbkdf2_sha256
from aiohttp_security import forget, remember
from aiohttp_security import check_permission, check_authorized
from auth_policy import check_credentials


class UserView(PydanticView):

    async def get(self) -> r200[List[schemas.UserOut]]:
        """
        Метод для получения всеx пользователей
        :return: json response
        """
        await check_permission(self.request, 'reading')
        users = session.query(User).all()
        result = [schemas.UserOut.from_orm(user).dict() for user in users]
        return web.json_response(result, content_type='application/json', status=200)

    async def post(self, user: schemas.UserIn) -> r201[schemas.UserOut]:
        """
        Метод для создания нового пользователя
        :param user: данные о пользователе
        :return: json response
        """
        await check_permission(self.request, 'admin')
        new_user = User(**user.dict())
        new_user.password = pbkdf2_sha256.hash(new_user.password)
        try:
            session.add(new_user)
            session.commit()
        except IntegrityError:
            session.rollback()
            return web.json_response('Ошибка! Такой пользователь уже есть!')
        return web.json_response(user.dict(), content_type='application/json', status=201)

    async def delete(self) -> r202:
        """
        Метод для удаления пользователя по id
        :return: json response
        """
        await check_permission(self.request, 'admin')
        user_id = self.request.match_info['user_id']
        session.query(User).filter(User.id == user_id).delete()
        session.commit()
        return web.json_response(text='Объект успешно удален!', content_type='application/json', status=202)

    async def put(self, user: schemas.BaseUser) -> r200[schemas.UserOut]:
        """
        Метод для обновления всех данных о пользователе
        :return: json response
        """
        await check_permission(self.request, 'admin')
        user_id = self.request.match_info['user_id']
        try:
            session.query(User).filter(User.id == user_id).update(
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


async def get_user(request) -> r200[List[schemas.UserOut]]:
    """
    Обработчик для получения пользователя по идентификатору
    """
    user = session.query(User).where(User.id == request.match_info['user_id']).one_or_none()
    if user:
        result = schemas.UserOut.from_orm(user).dict()
        return web.json_response(result, content_type='application/json', status=200)

    return web.json_response(text='Пользователь не найден', content_type='application/json', status=200)


class AuthorizationView(PydanticView):

    async def post(self, auth_user: schemas.Authorization):
        """ Авторизация пользователя по логину и паролю """
        invalid_resp = web.HTTPForbidden()
        if await check_credentials(auth_user.login, auth_user.password):
            response = web.HTTPFound("/")
            await remember(self.request, response, auth_user.login)
            raise response
        raise invalid_resp

    async def get(self):
        """ Выход из системы """
        await check_authorized(self.request)
        response = web.json_response(text='Вы вышли из системы')
        await forget(self.request, response)
        return response
