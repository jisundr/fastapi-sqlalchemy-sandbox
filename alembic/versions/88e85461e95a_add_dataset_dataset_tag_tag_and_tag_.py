"""add dataset, dataset_tag, tag and tag_category tables

Revision ID: 88e85461e95a
Revises: 
Create Date: 2023-08-07 15:30:39.897327+00:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '88e85461e95a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dataset',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dataset_description'), 'dataset', ['description'], unique=False)
    op.create_index(op.f('ix_dataset_id'), 'dataset', ['id'], unique=False)
    op.create_index(op.f('ix_dataset_name'), 'dataset', ['name'], unique=True)
    op.create_table('tag_category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('hex_color', sa.String(), nullable=False),
    sa.Column('rank', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tag_category_id'), 'tag_category', ['id'], unique=False)
    op.create_index(op.f('ix_tag_category_name'), 'tag_category', ['name'], unique=True)
    op.create_table('tag',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['tag_category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tag_id'), 'tag', ['id'], unique=False)
    op.create_index(op.f('ix_tag_name'), 'tag', ['name'], unique=True)
    op.create_table('dataset_tag',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('dataset_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.Column('is_filterable', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['dataset_id'], ['dataset.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dataset_tag_id'), 'dataset_tag', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_dataset_tag_id'), table_name='dataset_tag')
    op.drop_table('dataset_tag')
    op.drop_index(op.f('ix_tag_name'), table_name='tag')
    op.drop_index(op.f('ix_tag_id'), table_name='tag')
    op.drop_table('tag')
    op.drop_index(op.f('ix_tag_category_name'), table_name='tag_category')
    op.drop_index(op.f('ix_tag_category_id'), table_name='tag_category')
    op.drop_table('tag_category')
    op.drop_index(op.f('ix_dataset_name'), table_name='dataset')
    op.drop_index(op.f('ix_dataset_id'), table_name='dataset')
    op.drop_index(op.f('ix_dataset_description'), table_name='dataset')
    op.drop_table('dataset')
    # ### end Alembic commands ###
