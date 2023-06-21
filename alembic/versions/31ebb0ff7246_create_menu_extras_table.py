"""create menu extras table

Revision ID: 31ebb0ff7246
Revises: 1b51daa45b61
Create Date: 2023-06-21 19:05:11.218314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import func

revision = '31ebb0ff7246'
down_revision = '1b51daa45b61'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'menu_extras',
        sa.Column('id', sa.String(191), primary_key=True, autoincrement=False, unique=True),
        sa.Column('menu_id', sa.String(191), nullable=False),
        sa.Column('name', sa.String(191), nullable=False),
        sa.Column('price', sa.Double(), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=func.now(), nullable=True),
        sa.Column('updated_at', sa.DateTime, server_onupdate=func.now(), nullable=True),
        sa.Column('deleted_at', sa.DateTime, nullable=True)
    )

    op.create_foreign_key(None, 'menu_extras', 'menus', ['menu_id'], ['id'])


def downgrade() -> None:
    op.drop_table('menu_extras')
