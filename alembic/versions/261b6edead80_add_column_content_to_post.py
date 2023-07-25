"""add Column content to post 

Revision ID: 261b6edead80
Revises: da484a039167
Create Date: 2023-07-25 07:27:45.489222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '261b6edead80'
down_revision = 'da484a039167'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("post" , sa.Column("content" , sa.String(10000) , nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("post" , "content")
    pass
