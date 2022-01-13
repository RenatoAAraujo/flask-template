"""initial tables update

Revision ID: 1ae9b6a8632e
Revises: d6483d457e27
Create Date: 2021-02-27 20:46:00.064171

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1ae9b6a8632e'
down_revision = 'd6483d457e27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('city', 'status',
               existing_type=mysql.INTEGER(display_width=11),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.alter_column('country', 'status',
               existing_type=mysql.INTEGER(display_width=11),
               type_=sa.Boolean(),
               existing_nullable=False)
    op.alter_column('group', 'status',
               existing_type=mysql.INTEGER(display_width=11),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.alter_column('state', 'status',
               existing_type=mysql.INTEGER(display_width=11),
               type_=sa.Boolean(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('state', 'status',
               existing_type=sa.Boolean(),
               type_=mysql.INTEGER(display_width=11),
               existing_nullable=True)
    op.alter_column('group', 'status',
               existing_type=sa.Boolean(),
               type_=mysql.INTEGER(display_width=11),
               existing_nullable=True)
    op.alter_column('country', 'status',
               existing_type=sa.Boolean(),
               type_=mysql.INTEGER(display_width=11),
               existing_nullable=False)
    op.alter_column('city', 'status',
               existing_type=sa.Boolean(),
               type_=mysql.INTEGER(display_width=11),
               existing_nullable=True)
    # ### end Alembic commands ###
