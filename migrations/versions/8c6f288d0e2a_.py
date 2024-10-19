"""empty message

Revision ID: 8c6f288d0e2a
Revises: 6ac45bb14a78
Create Date: 2024-10-17 23:52:32.470349

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c6f288d0e2a'
down_revision = '6ac45bb14a78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('city', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('state', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('zipcode', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('language', sa.String(length=120), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('language')
        batch_op.drop_column('zipcode')
        batch_op.drop_column('state')
        batch_op.drop_column('city')

    # ### end Alembic commands ###