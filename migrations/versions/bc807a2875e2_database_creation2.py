"""Database creation2

Revision ID: bc807a2875e2
Revises: 
Create Date: 2024-02-19 23:15:00.821606

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc807a2875e2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('base_board',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('low', sa.Integer(), nullable=True),
    sa.Column('high', sa.Integer(), nullable=True),
    sa.Column('tags', sa.String(length=300), nullable=True),
    sa.Column('image', sa.String(length=300), nullable=False),
    sa.Column('points', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=100), nullable=False),
    sa.Column('games', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('base_board')
    # ### end Alembic commands ###