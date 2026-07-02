"""add tables

Revision ID: 5a69c3404281
Revises: 59cc77684558
Create Date: 2026-06-30 12:45:11.096019

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5a69c3404281'
down_revision: Union[str, Sequence[str], None] = '59cc77684558'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
