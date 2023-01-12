"""initial

Revision ID: f5c7f15ae8f5
Revises: 8654f5d78aad
Create Date: 2023-01-13 00:18:43.069910

"""
from alembic import op
import sqlalchemy as sa
from models import session, Permission, User
import datetime


# revision identifiers, used by Alembic.
revision = 'f5c7f15ae8f5'
down_revision = '8654f5d78aad'
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
    """ Удаление созданных записей в БД """
    admin = session.query(User).filter(User.id == 1).one()
    session.delete(admin)
    session.commit()
