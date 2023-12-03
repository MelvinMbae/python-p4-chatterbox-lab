"""Remove unique constraint from username column

Revision ID: fcb66d409bae
Revises: 43a7e9bc7d54
Create Date: 2023-12-03 14:58:47.531307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fcb66d409bae'
down_revision = '43a7e9bc7d54'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
