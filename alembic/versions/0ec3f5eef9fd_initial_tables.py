"""initial tables

Revision ID: 0ec3f5eef9fd
Revises: 96c8fdc064a2
Create Date: 2026-07-02 10:24:23.962304

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ec3f5eef9fd'
down_revision: Union[str, Sequence[str], None] = '96c8fdc064a2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
