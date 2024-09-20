"""empty message

Revision ID: f47dab47fade
Revises: 
Create Date: 2024-09-18 22:20:11.258957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f47dab47fade'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('caregiver',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('credentials', sa.String(length=120), nullable=False),
    sa.Column('experience', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=120), nullable=False),
    sa.Column('gender', sa.String(length=10), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('date_of_birth', sa.Date(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('emergencyContact', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('allergies', sa.String(length=120), nullable=True),
    sa.Column('bloodType', sa.String(length=120), nullable=True),
    sa.Column('hobbies', sa.String(length=300), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_current', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('caregiver_user',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('caregiver_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['caregiver_id'], ['caregiver.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('user_request_caregiver',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('caregiver_id', sa.Integer(), nullable=False),
    sa.Column('request_status', sa.String(length=80), nullable=False),
    sa.Column('date_time', sa.DateTime(), nullable=False),
    sa.Column('appointment_reason', sa.String(length=150), nullable=False),
    sa.ForeignKeyConstraint(['caregiver_id'], ['caregiver.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_request_caregiver')
    op.drop_table('caregiver_user')
    op.drop_table('user')
    op.drop_table('caregiver')
    # ### end Alembic commands ###