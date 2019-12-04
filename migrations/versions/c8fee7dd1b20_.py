"""empty message

Revision ID: c8fee7dd1b20
Revises: 150eaa16764c
Create Date: 2019-11-16 22:53:42.834718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8fee7dd1b20'
down_revision = '150eaa16764c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('team', sa.Column('lftm', sa.Boolean(create_constraint=False), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('team', 'lftm')
    # ### end Alembic commands ###
