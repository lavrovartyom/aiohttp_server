"""empty message

Revision ID: 96cd49dcfc14
Revises: b1e89b6c6808
Create Date: 2023-01-12 00:34:40.899132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96cd49dcfc14'
down_revision = 'b1e89b6c6808'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'permission',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'permission',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###