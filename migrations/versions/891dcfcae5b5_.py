"""empty message

Revision ID: 891dcfcae5b5
Revises: fc1c93b9400b
Create Date: 2020-07-17 06:12:41.298210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '891dcfcae5b5'
down_revision = 'fc1c93b9400b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=True),
    sa.Column('venue_id', sa.Integer(), nullable=True),
    sa.Column('starting_date', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('show')
    # ### end Alembic commands ###
