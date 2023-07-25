"""compelet post column

Revision ID: f0c2863a0ed4
Revises: 84a09a5e7f00
Create Date: 2023-07-25 07:53:56.773098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0c2863a0ed4'
down_revision = '84a09a5e7f00'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("post" , sa.Column("published" , sa.Boolean() , nullable=False , default="TRUE"))
    op.add_column("post",sa.Column("created_at" , sa.TIMESTAMP(timezone=True), server_default=sa.text('now()') , nullable=False))


def downgrade() -> None:
    op.drop_column("post" , "published")
    op.drop_column("post" , "created_at")
    pass
