"""criar tabelas iniciais

Revision ID: 14f684fef53b
Revises: 5a69c3404281
Create Date: 2026-06-30 12:50:14.695941

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '14f684fef53b'
down_revision: Union[str, Sequence[str], None] = '5a69c3404281'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
