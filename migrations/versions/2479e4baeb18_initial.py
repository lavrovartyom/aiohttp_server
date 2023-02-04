"""initial

Revision ID: 2479e4baeb18
Revises: fb712e94a930
Create Date: 2023-01-23 22:58:05.353125

"""
import datetime
from app.db import session
from app.models import Permission, User
from passlib.hash import pbkdf2_sha256

# revision identifiers, used by Alembic.
revision = '2479e4baeb18'
down_revision = 'fb712e94a930'
branch_labels = None
depends_on = 'fb712e94a930'


def upgrade() -> None:
    """
    Миграция для создания администратора, а также прав пользователя
    """
    hashing_password = pbkdf2_sha256.hash('admin')
    with session.begin():
        session.add_all(
            [
                Permission(permission='admin'),
                Permission(permission='reading'),
                Permission(permission='blocking')
            ]
        )
        session.flush()
        admin_user = User(
            first_name='admin',
            last_name='admin',
            login='admin',
            password=hashing_password,
            date_of_birth=datetime.date(1970, 1, 1),
            permission='admin'
        )
        session.add(admin_user)
        session.commit()


def downgrade() -> None:
    """
    Удаление созданных записей в БД
    """
    with session.begin():
        session.query(User).delete()
        session.query(Permission).delete()
        session.commit()
