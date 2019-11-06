"""empty message

Revision ID: 52ee36b9b4b5
Revises: 
Create Date: 2019-11-05 17:45:06.685850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52ee36b9b4b5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team', sa.String(length=20), nullable=True),
    sa.Column('player1', sa.String(length=30), nullable=True),
    sa.Column('player2', sa.String(length=30), nullable=True),
    sa.Column('player3', sa.String(length=30), nullable=True),
    sa.Column('swimming', sa.Float(precision=3, asdecimal=2), nullable=True),
    sa.Column('cycling', sa.Float(precision=5, asdecimal=2), nullable=True),
    sa.Column('running', sa.Float(precision=4, asdecimal=2), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('team')
    )
    op.create_table('users',
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('email', sa.String(length=40), nullable=True),
    sa.Column('password', sa.String(length=80), nullable=True),
    sa.Column('teamid', sa.String(length=20), nullable=True),
    sa.Column('bio', sa.String(length=200), nullable=True),
    sa.Column('lft', sa.Boolean(create_constraint=False), nullable=True),
    sa.Column('swimming', sa.Float(precision=3, asdecimal=2), nullable=True),
    sa.Column('cycling', sa.Float(precision=5, asdecimal=2), nullable=True),
    sa.Column('running', sa.Float(precision=4, asdecimal=2), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('team')
    # ### end Alembic commands ###