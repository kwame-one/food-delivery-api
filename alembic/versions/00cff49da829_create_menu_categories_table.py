"""create menu categories table

Revision ID: 00cff49da829
Revises: 40581de9efb2
Create Date: 2023-06-21 18:51:20.088624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import String, func

revision = '00cff49da829'
down_revision = '40581de9efb2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'menu_categories',
        sa.Column('id', String(191), primary_key=True, unique=True),
        sa.Column('name', String(191), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=func.now(), nullable=True),
        sa.Column('updated_at', sa.DateTime, server_onupdate=func.now(), nullable=True),
        sa.Column('deleted_at', sa.DateTime, nullable=True)
    )


def downgrade() -> None:
    op.drop_table('menu_categories')
