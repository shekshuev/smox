"""updated

Revision ID: c9b956b198e9
Revises: 0ea7839a2324
Create Date: 2021-02-21 16:53:36.833133

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9b956b198e9'
down_revision = '0ea7839a2324'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('target',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('keywords', sa.Text(), nullable=False),
    sa.Column('begin_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('target_source',
    sa.Column('source_id', sa.Integer(), nullable=False),
    sa.Column('target_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['source_id'], ['source.id'], ),
    sa.ForeignKeyConstraint(['target_id'], ['target.id'], ),
    sa.PrimaryKeyConstraint('source_id', 'target_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('target_source')
    op.drop_table('target')
    # ### end Alembic commands ###
