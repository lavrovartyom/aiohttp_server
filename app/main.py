from aiohttp_session import SimpleCookieStorage, session_middleware
from aiohttp import web
from aiohttp_security import SessionIdentityPolicy, setup as setup_security
from auth_policy import DBAuthorizationPolicy
from views import AuthorizationView, UserView, get_user
import logging


async def make_up():
    logging.basicConfig(level=logging.DEBUG)
    middleware = session_middleware(SimpleCookieStorage())
    app = web.Application(middlewares=[middleware])
    app.add_routes(
        [
            web.get('/', UserView),
            web.get('/get/{user_id}', get_user),
            web.post('/create', UserView),
            web.delete('/delete/{user_id}', UserView),
            web.put('/update/{user_id}', UserView),
            web.post('/login', AuthorizationView),
            web.get('/logout', AuthorizationView)
        ]
    )
    policy = SessionIdentityPolicy()
    setup_security(app, policy, DBAuthorizationPolicy())
    return app

if __name__ == '__main__':
    web.run_app(make_up())
