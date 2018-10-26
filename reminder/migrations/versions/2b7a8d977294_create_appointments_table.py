from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b7a8d977294'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'appointments',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('phone_number', sa.String(20), nullable=False),
        sa.Column('delta', sa.Integer, nullable=False),
        sa.Column('time', sa.DateTime, nullable=False),
        sa.Column('timezone', sa.String(), nullable=False),
    )


def downgrade():
    op.drop_table('appointments')
