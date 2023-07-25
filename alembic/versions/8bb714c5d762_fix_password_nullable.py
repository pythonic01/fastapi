"""fix password nullable

Revision ID: 8bb714c5d762
Revises: 54715d56fb06
Create Date: 2023-07-25 08:19:41.330102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bb714c5d762'
down_revision = '54715d56fb06'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('users', 'password', nullable=True)

def downgrade() -> None:
    op.alter_column('users', 'password', nullable=False)
