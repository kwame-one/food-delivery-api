"""create restaurant registrations

Revision ID: 8bcdffb5b5aa
Revises: d7469dc92195
Create Date: 2023-06-21 22:29:07.706518

"""
import sqlalchemy as sa
from alembic import op
# revision identifiers, used by Alembic.
from sqlalchemy import func


revision = '8bcdffb5b5aa'
down_revision = 'd7469dc92195'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'restaurant_registrations',
        sa.Column('id', sa.String(191), primary_key=True, autoincrement=False, unique=True),
        sa.Column('restaurant_name', sa.String(191), nullable=False),
        sa.Column('restaurant_email', sa.String(191), nullable=False),
        sa.Column('restaurant_phone', sa.String(191), nullable=False),
        sa.Column('restaurant_address', sa.String(191), nullable=False),
        sa.Column('user_name', sa.String(191), nullable=False),
        sa.Column('user_email', sa.String(191), nullable=False),
        sa.Column('status', sa.String(191), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=func.now(), nullable=True),
        sa.Column('updated_at', sa.DateTime, server_onupdate=func.now(), nullable=True),
        sa.Column('deleted_at', sa.DateTime, nullable=True)
    )


def downgrade() -> None:
    op.drop_table('restaurant_registrations')
