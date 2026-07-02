"""add tables

Revision ID: 59cc77684558
Revises: 7ebb424285ce
Create Date: 2026-06-30 12:42:06.290995

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59cc77684558'
down_revision: Union[str, Sequence[str], None] = '7ebb424285ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
