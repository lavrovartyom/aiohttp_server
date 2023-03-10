from app.models import User
from app.db import session
from aiohttp_security.abc import AbstractAuthorizationPolicy
from passlib.hash import pbkdf2_sha256


class DBAuthorizationPolicy(AbstractAuthorizationPolicy):

    async def authorized_userid(self, identity):
        """
        Проверка на наличие пользователя в бд
        """
        user = session.query(User).where(User.login == identity).one_or_none()
        if user:
            return identity
        return None

    async def permits(self, identity, permission, context=None):
        """
        Проверка прав пользователя
        """
        user = session.query(User).where(User.login == identity).one_or_none()
        if user.permission == permission or user.permission == 'admin':
            return True
        return False


async def check_credentials(login: str, password: str) -> bool:
    """
    Проверка пароля пользователя при авторизации
    """
    user = session.query(User).where(User.login == login).one_or_none()
    if user:
        return pbkdf2_sha256.verify(password, user.password)
    return False
