"""create order items table

Revision ID: d7469dc92195
Revises: 2695b9a3eb7f
Create Date: 2023-06-21 19:22:33.988030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import func

revision = 'd7469dc92195'
down_revision = '2695b9a3eb7f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'order_items',
        sa.Column('id', sa.String(191), primary_key=True, autoincrement=False, unique=True),
        sa.Column('order_id', sa.String(191), nullable=False),
        sa.Column('menu_id', sa.String(191), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.Column('menu_price', sa.Double(), nullable=False),
        sa.Column('menu_extras', sa.TEXT(), nullable=True),
        sa.Column('created_at', sa.DateTime, server_default=func.now(), nullable=True),
        sa.Column('updated_at', sa.DateTime, server_onupdate=func.now(), nullable=True),
        sa.Column('deleted_at', sa.DateTime, nullable=True)
    )

    op.create_foreign_key(None, 'order_items', 'orders', ['order_id'], ['id'])
    op.create_foreign_key(None, 'order_items', 'menus', ['menu_id'], ['id'])


def downgrade() -> None:
    op.drop_table('order_items')
