"""create order statuses table

Revision ID: 3cee1d8cf464
Revises: 31ebb0ff7246
Create Date: 2023-06-21 19:15:07.660864

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import func

revision = '3cee1d8cf464'
down_revision = '31ebb0ff7246'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'order_statuses',
        sa.Column('id', sa.String(191), primary_key=True, autoincrement=False, unique=True),
        sa.Column('name', sa.String(191), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=func.now(), nullable=True),
        sa.Column('updated_at', sa.DateTime, server_onupdate=func.now(), nullable=True),
        sa.Column('deleted_at', sa.DateTime, nullable=True)
    )


def downgrade() -> None:
    op.drop_table('order_statuses')
