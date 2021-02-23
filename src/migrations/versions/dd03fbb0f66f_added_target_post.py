"""added target post

Revision ID: dd03fbb0f66f
Revises: 617f8d9b15a1
Create Date: 2021-02-23 02:06:40.720894

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dd03fbb0f66f'
down_revision = '617f8d9b15a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('target_post',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('target_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['target_id'], ['target.id'], ),
    sa.PrimaryKeyConstraint('post_id', 'target_id')
    )
    op.drop_table('target_source')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('target_source',
    sa.Column('source_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('target_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['source_id'], ['source.id'], name='target_source_ibfk_1'),
    sa.ForeignKeyConstraint(['target_id'], ['target.id'], name='target_source_ibfk_2'),
    sa.PrimaryKeyConstraint('source_id', 'target_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('target_post')
    # ### end Alembic commands ###