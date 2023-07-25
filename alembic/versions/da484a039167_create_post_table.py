"""create post table

Revision ID: da484a039167
Revises: 
Create Date: 2023-07-25 07:03:09.931409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da484a039167'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('post', sa.Column('id' , sa.Integer() ,nullable=False , primary_key=True )
                    ,sa.Column('title' , sa.String(1000) , nullable=False))
    pass

def downgrade() -> None:
    op.drop_column("post")
    pass