"""criar_tabelas_reais

Revision ID: d14e6045d8aa
Revises: 14f684fef53b
Create Date: 2026-06-30 12:51:46.145629

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd14e6045d8aa'
down_revision: Union[str, Sequence[str], None] = '14f684fef53b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
