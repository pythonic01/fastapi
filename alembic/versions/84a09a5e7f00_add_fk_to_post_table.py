"""add fk to post table

Revision ID: 84a09a5e7f00
Revises: e4613f628211
Create Date: 2023-07-25 07:46:50.961634

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84a09a5e7f00'
down_revision = 'e4613f628211'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("post" , sa.Column("woner_id" , sa.Integer() , nullable=False))
    op.create_foreign_key('post_user_fk' , source_table="post" , referent_table="users" , local_cols=["woner_id"]
                          ,remote_cols=['id'] , ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_user_fk' ,table_name="post")
    op.drop_column("post" , "woner_id")
    pass
