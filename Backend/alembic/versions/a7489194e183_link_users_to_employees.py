"""link users to employees

Revision ID: a7489194e183
Revises: 17f0532e2435
Create Date: 2026-09-30 15:12:42.026564

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "a7489194e183"
down_revision: Union[str, Sequence[str], None] = "17f0532e2435"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_foreign_key(
        "fk_users_employee_id_employees",
        "users",
        "employees",
        ["employee_id"],
        ["employee_id"]
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        "fk_users_employee_id_employees",
        "users",
        type_="foreignkey"
    )