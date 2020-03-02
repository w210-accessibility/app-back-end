"""added column to specify right vs left

Revision ID: f3b2087436af
Revises: 0a7e686eeb18
Create Date: 2020-03-01 10:52:10.390276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3b2087436af'
down_revision = '0a7e686eeb18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sidewalk_segment2', sa.Column('whichArcgisFile', sa.String(length=10)))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sidewalk_segment2', 'whichArcgisFile')
    # ### end Alembic commands ###