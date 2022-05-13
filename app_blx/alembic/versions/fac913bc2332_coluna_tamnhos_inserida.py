"""Coluna tamnhos inserida

Revision ID: fac913bc2332
Revises: 264ba2455774
Create Date: 2022-04-26 21:21:12.998303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fac913bc2332'
down_revision = '264ba2455774'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('produto', sa.Column('tamanhos', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('produto', 'tamanhos')
    # ### end Alembic commands ###
