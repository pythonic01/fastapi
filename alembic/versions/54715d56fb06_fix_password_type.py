"""fix password type

Revision ID: 54715d56fb06
Revises: 189c8fa21fa3
Create Date: 2023-07-25 08:17:29.874382

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54715d56fb06'
down_revision = '189c8fa21fa3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('users', 'password', type_=sa.String(1000))


def downgrade() -> None:
    op.alter_column('users' , 'password' , type_=sa.Integer())
