"""removed log table

Revision ID: 199333d2ea06
Revises: f2769554e0ec
Create Date: 2021-03-13 11:43:51.268197

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '199333d2ea06'
down_revision = 'f2769554e0ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('log')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('log',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('message', mysql.TEXT(), nullable=False),
    sa.Column('datetime', mysql.DATETIME(), nullable=False),
    sa.Column('type', mysql.SMALLINT(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
