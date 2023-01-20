"""Creacion de categorias mode v2

Revision ID: a7da27019bfe
Revises: a6ede0d82507
Create Date: 2023-01-19 21:53:55.255123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7da27019bfe'
down_revision = 'a6ede0d82507'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('categorias', schema=None) as batch_op:
        batch_op.add_column(sa.Column('estado', sa.Boolean(), nullable=True))

    with op.batch_alter_table('productos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('estado', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('productos', schema=None) as batch_op:
        batch_op.drop_column('estado')

    with op.batch_alter_table('categorias', schema=None) as batch_op:
        batch_op.drop_column('estado')

    # ### end Alembic commands ###
