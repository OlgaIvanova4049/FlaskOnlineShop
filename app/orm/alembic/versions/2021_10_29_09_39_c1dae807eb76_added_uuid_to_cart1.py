"""added uuid to cart1

Revision ID: c1dae807eb76
Revises: ed3c197c6837
Create Date: 2021-10-29 09:39:55.966976

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c1dae807eb76'
down_revision = 'ed3c197c6837'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('crt_cart', sa.Column('uid', postgresql.UUID(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('crt_cart', 'uid')
    # ### end Alembic commands ###
