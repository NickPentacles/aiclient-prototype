"""init

Revision ID: 0fd624ed9f30
Revises: 
Create Date: 2024-10-07 17:22:05.906944

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0fd624ed9f30'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project',
    sa.Column('uuid', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('chat',
    sa.Column('uuid', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('tokens', sa.Integer(), nullable=False),
    sa.Column('project_uuid', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['project_uuid'], ['project.uuid'], ),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('file',
    sa.Column('uuid', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('content', sa.String(length=6000), nullable=False),
    sa.Column('path', sa.String(length=100), nullable=False),
    sa.Column('project_uuid', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['project_uuid'], ['project.uuid'], ),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('message',
    sa.Column('uuid', sa.UUID(), nullable=False),
    sa.Column('role', sa.String(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('tokens', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('chat_uuid', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['chat_uuid'], ['chat.uuid'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('message')
    op.drop_table('file')
    op.drop_table('chat')
    op.drop_table('project')
    # ### end Alembic commands ###
