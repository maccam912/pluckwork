"""Add timestamps

Revision ID: 91a2d26342cb
Revises: 9417b0cfb6ab
Create Date: 2024-01-02 11:36:01.550389

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '91a2d26342cb'
down_revision: Union[str, None] = '9417b0cfb6ab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('reserved_at', sa.DateTime(), nullable=True))
    op.add_column('tasks', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.add_column('tasks', sa.Column('updated_at', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'updated_at')
    op.drop_column('tasks', 'created_at')
    op.drop_column('tasks', 'reserved_at')
    # ### end Alembic commands ###
