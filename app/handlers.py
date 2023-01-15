from aiohttp import web
from models import User
from db import session


routes = web.RouteTableDef()


@routes.get('/')
async def get_all_user(request):
    """ Функция обработчик. Получение пользователей """
    users = session.query(User).all()
    return web.json_response()
