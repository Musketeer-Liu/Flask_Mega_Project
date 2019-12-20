"""add language to posts

Revision ID: 6798e5993805
Revises: 9827e49c8048
Create Date: 2019-12-18 23:35:24.911951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6798e5993805'
down_revision = '9827e49c8048'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###