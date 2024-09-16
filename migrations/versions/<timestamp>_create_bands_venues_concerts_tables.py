# migrations/versions/<timestamp>_create_bands_venues_concerts_tables.py
from alembic import op
import sqlalchemy as sa

revision = '<timestamp>'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'bands',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('hometown', sa.String, nullable=False),
    )
    op.create_table(
        'venues',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('city', sa.String, nullable=False),
    )
    op.create_table(
        'concerts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('date', sa.String, nullable=False),
        sa.Column('band_id', sa.Integer, sa.ForeignKey('bands.id'), nullable=False),
        sa.Column('venue_id', sa.Integer, sa.ForeignKey('venues.id'), nullable=False),
    )

def downgrade():
    op.drop_table('concerts')
    op.drop_table('venues')
    op.drop_table('bands')
