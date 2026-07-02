"""create tables

Revision ID: 96c8fdc064a2
Revises: d14e6045d8aa
Create Date: 2026-07-02 10:23:17.772075

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '96c8fdc064a2'
down_revision: Union[str, Sequence[str], None] = 'd14e6045d8aa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
