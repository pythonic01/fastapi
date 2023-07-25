"""create users table

Revision ID: e4613f628211
Revises: 261b6edead80
Create Date: 2023-07-25 07:35:17.405276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4613f628211'
down_revision = '261b6edead80'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users" , sa.Column("id" , sa.Integer() , nullable=False , primary_key=True)
                    ,sa.Column("email" , sa.String(200) , nullable=False , unique=True)
                    ,sa.Column("password" , sa.String(1000) , nullable=False)
                    ,sa.Column("created_at" , sa.TIMESTAMP(timezone=True), server_default=sa.text('now()') , nullable=False)
    )



def downgrade() -> None:
    op.drop_table("users")
    pass
