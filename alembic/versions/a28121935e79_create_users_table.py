"""create users table

Revision ID: a28121935e79
Revises: decc327b2d55
Create Date: 2023-06-21 16:41:09.480697

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
from sqlalchemy import func

revision = 'a28121935e79'
down_revision = 'decc327b2d55'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.String(191), primary_key=True, autoincrement=False, unique=True),
        sa.Column('name', sa.String(191), nullable=False),
        sa.Column('email', sa.String(191), nullable=False),
        sa.Column('password', sa.String(191), nullable=False),
        sa.Column('role_id', sa.String(191), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=func.now(), nullable=True),
        sa.Column('updated_at', sa.DateTime, server_onupdate=func.now(), nullable=True),
        sa.Column('deleted_at', sa.DateTime, nullable=True)
    )

    op.create_foreign_key(
        None,
        'users',
        'roles',
        ['role_id'],
        ['id']
    )


def downgrade() -> None:
    op.drop_table('users')
