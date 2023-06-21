"""create restaurants table

Revision ID: 40581de9efb2
Revises: a28121935e79
Create Date: 2023-06-21 17:05:27.822858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import func

revision = '40581de9efb2'
down_revision = 'a28121935e79'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'restaurants',
        sa.Column('id', sa.String(191), primary_key=True, autoincrement=False, unique=True),
        sa.Column('name', sa.String(191), nullable=False),
        sa.Column('email', sa.String(191), nullable=False),
        sa.Column('address', sa.String(191), nullable=False),
        sa.Column('phone', sa.String(191), nullable=False),
        sa.Column('user_id', sa.String(191), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=func.now(), nullable=True),
        sa.Column('updated_at', sa.DateTime, server_onupdate=func.now(), nullable=True),
        sa.Column('deleted_at', sa.DateTime, nullable=True)
    )

    op.create_foreign_key(None, 'restaurants', 'users', ['user_id'], ['id'])


def downgrade() -> None:
    op.drop_table('restaurants')
