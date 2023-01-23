"""initial

Revision ID: 2479e4baeb18
Revises: fb712e94a930
Create Date: 2023-01-23 22:58:05.353125

"""
from alembic import op
import sqlalchemy as sa
import datetime
from db import session
from models import Permission, User
from app.logic import hash_password

# revision identifiers, used by Alembic.
revision = '2479e4baeb18'
down_revision = 'fb712e94a930'
branch_labels = None
depends_on = None


def upgrade() -> None:
    """
    Миграция для создания администратора, а также прав пользователя
    """
    hashing_password = hash_password('admin')
    with session.begin():
        session.add_all(
            [
                Permission(permission='Администратор'),
                Permission(permission='Только чтение'),
                Permission(permission='Блокировка')
            ]
        )
        session.flush()
        admin_user = User(
            first_name='admin',
            last_name='admin',
            login='admin',
            password=hashing_password,
            date_of_birth=datetime.date(1970, 1, 1),
            permission='Администратор'
        )
        session.add(admin_user)
        session.commit()


def downgrade() -> None:
    """
    Удаление созданных записей в БД
    """
    with session.begin():
        session.query(User).filter(User.login == 'admin').delete()
        session.query(Permission).delete()
        session.commit()
