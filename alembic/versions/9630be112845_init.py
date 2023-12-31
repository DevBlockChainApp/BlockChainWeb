"""Init

Revision ID: 9630be112845
Revises: 
Create Date: 2023-12-16 12:33:29.532912

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9630be112845'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('create schema bchain')
    op.create_table('t_block',
    sa.Column('index', sa.Integer(), nullable=False),
    sa.Column('data', sa.String(), nullable=True),
    sa.Column('date_create', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.Column('hash_block', sa.String(), nullable=True),
    sa.Column('prev_hash', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('index'),
    schema='bchain',
    comment='Main chain table'
    )
    op.create_index(op.f('ix_bchain_t_block_data'), 't_block', ['data'], unique=False, schema='bchain')
    op.create_index(op.f('ix_bchain_t_block_hash_block'), 't_block', ['hash_block'], unique=True, schema='bchain')
    op.create_index(op.f('ix_bchain_t_block_index'), 't_block', ['index'], unique=False, schema='bchain')
    op.create_index(op.f('ix_bchain_t_block_prev_hash'), 't_block', ['prev_hash'], unique=True, schema='bchain')


def downgrade() -> None:
    op.drop_index(op.f('ix_bchain_t_block_prev_hash'), table_name='t_block', schema='bchain')
    op.drop_index(op.f('ix_bchain_t_block_index'), table_name='t_block', schema='bchain')
    op.drop_index(op.f('ix_bchain_t_block_hash_block'), table_name='t_block', schema='bchain')
    op.drop_index(op.f('ix_bchain_t_block_data'), table_name='t_block', schema='bchain')
    op.drop_table('t_block', schema='bchain')
    op.execute('drop schema bchain')
