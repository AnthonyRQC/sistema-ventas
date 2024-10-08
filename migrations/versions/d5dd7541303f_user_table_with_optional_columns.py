"""User table with optional columns

Revision ID: d5dd7541303f
Revises: f7f27cbaecc7
Create Date: 2024-07-26 15:53:07.576050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5dd7541303f'
down_revision = 'f7f27cbaecc7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
        batch_op.alter_column('document_number',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('first_name',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
        batch_op.alter_column('last_name',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('last_name',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
        batch_op.alter_column('first_name',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
        batch_op.alter_column('document_number',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)

    # ### end Alembic commands ###
