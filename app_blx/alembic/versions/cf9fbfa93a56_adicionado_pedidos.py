"""Adicionado Pedidos

Revision ID: cf9fbfa93a56
Revises: 4c1527ecb78c
Create Date: 2022-05-08 19:01:09.259679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf9fbfa93a56'
down_revision = '4c1527ecb78c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pedido', schema=None) as batch_op:
        batch_op.add_column(sa.Column('quantidade', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('local_entrega', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('tipo_entrega', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('observacao', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('usuario_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('produto_id', sa.Integer(), nullable=True))
        batch_op.create_index(batch_op.f('ix_pedido_id'), ['id'], unique=False)
        batch_op.create_foreign_key('fk_pedido_usuario', 'usuario', ['usuario_id'], ['id'])
        batch_op.create_foreign_key('fk_pedido_produto', 'produto', ['produto_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pedido', schema=None) as batch_op:
        batch_op.drop_constraint('fk_pedido_produto', type_='foreignkey')
        batch_op.drop_constraint('fk_pedido_usuario', type_='foreignkey')
        batch_op.drop_index(batch_op.f('ix_pedido_id'))
        batch_op.drop_column('produto_id')
        batch_op.drop_column('usuario_id')
        batch_op.drop_column('observacao')
        batch_op.drop_column('tipo_entrega')
        batch_op.drop_column('local_entrega')
        batch_op.drop_column('quantidade')

    # ### end Alembic commands ###
