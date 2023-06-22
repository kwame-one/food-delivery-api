"""create menus table

Revision ID: 1b51daa45b61
Revises: 00cff49da829
Create Date: 2023-06-21 18:55:26.095401

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import String, func, Double, Text

revision = '1b51daa45b61'
down_revision = '00cff49da829'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'menus',
        sa.Column('id', String(191), primary_key=True, autoincrement=False, unique=True),
        sa.Column('menu_category_id', String(191), nullable=False),
        sa.Column('restaurant_id', String(191), nullable=False),
        sa.Column('name', String(191), nullable=False),
        sa.Column('description', Text(), nullable=False),
        sa.Column('price', Double(), nullable=False),
        sa.Column('image', String(191), nullable=True),
        sa.Column('created_at', sa.DateTime, server_default=func.now(), nullable=True),
        sa.Column('updated_at', sa.DateTime, server_onupdate=func.now(), nullable=True),
        sa.Column('deleted_at', sa.DateTime, nullable=True)
    )

    op.create_foreign_key(None, 'menus', 'menu_categories', ['menu_category_id'], ['id'])
    op.create_foreign_key(None, 'menus', 'restaurants', ['restaurant_id'], ['id'])


def downgrade() -> None:
    op.drop_table('menus')
