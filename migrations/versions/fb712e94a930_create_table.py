"""create_table

Revision ID: fb712e94a930
Revises: 
Create Date: 2023-01-23 22:56:34.957123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb712e94a930'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('permission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('permission', sa.String(length=25), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('permission')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('login', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=500), nullable=False),
    sa.Column('date_of_birth', sa.Date(), nullable=True),
    sa.Column('permission', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['permission'], ['permission.permission'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('login')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('permission')
    # ### end Alembic commands ###