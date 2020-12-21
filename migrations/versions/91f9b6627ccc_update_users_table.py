"""update_users_table

Revision ID: 91f9b6627ccc
Revises: 3bd63c80ff70
Create Date: 2020-12-18 11:57:59.799591

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '91f9b6627ccc'
down_revision = '3bd63c80ff70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employees', sa.Column('user_id', mysql.INTEGER(), nullable=True))
    op.create_foreign_key(None, 'employees', 'users', ['user_id'], ['id'])
    op.add_column('users', sa.Column('employee_id', mysql.INTEGER(), nullable=True))
    op.create_foreign_key(None, 'users', 'employees', ['employee_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'employee_id')
    op.drop_constraint(None, 'employees', type_='foreignkey')
    op.drop_column('employees', 'user_id')
    # ### end Alembic commands ###
