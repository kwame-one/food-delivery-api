"""create user orders table

Revision ID: fe54e838365d
Revises: 3cee1d8cf464
Create Date: 2023-06-21 19:17:12.208847

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import func

revision = 'fe54e838365d'
down_revision = '3cee1d8cf464'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'user_orders',
        sa.Column('id', sa.String(191), primary_key=True, autoincrement=False, unique=True),
        sa.Column('user_id', sa.String(191), nullable=False),
        sa.Column('total', sa.Double(), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=func.now(), nullable=True),
        sa.Column('updated_at', sa.DateTime, server_onupdate=func.now(), nullable=True),
        sa.Column('deleted_at', sa.DateTime, nullable=True)
    )

    op.create_foreign_key(None, 'user_orders', 'users', ['user_id'], ['id'])


def downgrade() -> None:
    op.drop_table('user_orders')
