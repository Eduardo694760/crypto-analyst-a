"""initial tables

Revision ID: 3e49211c3d77
Revises: 0ec3f5eef9fd
Create Date: 2026-07-02 10:25:53.286018

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e49211c3d77'
down_revision: Union[str, Sequence[str], None] = '0ec3f5eef9fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
