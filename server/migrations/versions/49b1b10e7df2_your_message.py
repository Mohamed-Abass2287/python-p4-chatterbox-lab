"""your message

Revision ID: 49b1b10e7df2
Revises: 
Create Date: 2025-06-15 12:02:48.279514

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49b1b10e7df2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('message')
    # ### end Alembic commands ###
