"""empty message

Revision ID: 70f7ccf8e1e8
Revises: f5681ddf90d2
Create Date: 2019-11-20 14:17:23.486086

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70f7ccf8e1e8'
down_revision = 'f5681ddf90d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('team', sa.Column('email1', sa.String(length=40), nullable=True))
    op.add_column('team', sa.Column('email2', sa.String(length=40), nullable=True))
    op.add_column('team', sa.Column('email3', sa.String(length=40), nullable=True))
    op.add_column('team', sa.Column('password', sa.String(length=40), nullable=True))
    op.drop_constraint('team_email_key', 'team', type_='unique')
    op.create_unique_constraint(None, 'team', ['email3'])
    op.create_unique_constraint(None, 'team', ['email2'])
    op.create_unique_constraint(None, 'team', ['email1'])
    op.drop_column('team', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('team', sa.Column('email', sa.VARCHAR(length=40), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'team', type_='unique')
    op.drop_constraint(None, 'team', type_='unique')
    op.drop_constraint(None, 'team', type_='unique')
    op.create_unique_constraint('team_email_key', 'team', ['email'])
    op.drop_column('team', 'password')
    op.drop_column('team', 'email3')
    op.drop_column('team', 'email2')
    op.drop_column('team', 'email1')
    # ### end Alembic commands ###
