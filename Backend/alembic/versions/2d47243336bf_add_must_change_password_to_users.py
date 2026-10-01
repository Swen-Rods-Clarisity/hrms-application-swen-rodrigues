"""add must change password to users

Revision ID: 2d47243336bf
Revises: a7489194e183
Create Date: 2026-10-01 14:42:21.861593

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2d47243336bf'
down_revision: Union[str, Sequence[str], None] = 'a7489194e183'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column(
        "users",
        sa.Column(
            "must_change_password",
            sa.Boolean(),
            nullable=False,
            server_default=sa.true()
        )
    )

    op.alter_column(
        "users",
        "must_change_password",
        server_default=None
    )