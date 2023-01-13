"""initial

Revision ID: 443f6cf9f620
Revises: 0dad2b1c8ad3
Create Date: 2023-01-14 00:35:53.255777

"""
from alembic import op
import sqlalchemy as sa
import datetime
from db import session
from models import Permission, User


# revision identifiers, used by Alembic.
revision = '443f6cf9f620'
down_revision = '0dad2b1c8ad3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    """
    Миграция для создания администратора, а также прав пользователя
    """
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
            password='admin',
            date_of_birth=datetime.date(1970, 1, 1),
            permission=1
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
