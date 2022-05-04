"""criado tabela de usuarios e realcionamentos

Revision ID: 70661685b49d
Revises: fac913bc2332
Create Date: 2022-04-28 23:02:19.179436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70661685b49d'
down_revision = 'fac913bc2332'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('produto', schema=None) as batch_op:
        batch_op.create_foreign_key('FK_usuario', 'usuario', ['usuario_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('produto', schema=None) as batch_op:
        batch_op.drop_constraint('FK_usuario', type_='foreignkey')

    # ### end Alembic commands ###