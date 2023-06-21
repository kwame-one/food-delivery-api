"""create orders table

Revision ID: 2695b9a3eb7f
Revises: fe54e838365d
Create Date: 2023-06-21 19:18:44.226522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import func

revision = '2695b9a3eb7f'
down_revision = 'fe54e838365d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'orders',
        sa.Column('id', sa.String(191), primary_key=True, autoincrement=False, unique=True),
        sa.Column('order_number', sa.String(191), nullable=False),
        sa.Column('user_id', sa.String(191), nullable=False),
        sa.Column('user_order_id', sa.String(191), nullable=False),
        sa.Column('restaurant_id', sa.String(191), nullable=False),
        sa.Column('order_status_id', sa.String(191), nullable=False),
        sa.Column('total', sa.Double(), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=func.now(), nullable=True),
        sa.Column('updated_at', sa.DateTime, server_onupdate=func.now(), nullable=True),
        sa.Column('deleted_at', sa.DateTime, nullable=True)
    )

    op.create_foreign_key(None, 'orders', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'orders', 'restaurants', ['restaurant_id'], ['id'])
    op.create_foreign_key(None, 'orders', 'order_statuses', ['order_status_id'], ['id'])
    op.create_foreign_key(None, 'orders', 'user_orders', ['user_order_id'], ['id'])


def downgrade() -> None:
    op.drop_table('orders')
