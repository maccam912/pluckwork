"""create tasks table

Revision ID: 9417b0cfb6ab
Revises: 
Create Date: 2024-01-02 10:28:22.474770

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9417b0cfb6ab'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'tasks',
        sa.Column('id', sa.String(), primary_key=True),
        sa.Column('input', sa.LargeBinary(), nullable=False),
        sa.Column('output', sa.LargeBinary(), nullable=True)
    )


def downgrade() -> None:
    op.drop_table('tasks')
