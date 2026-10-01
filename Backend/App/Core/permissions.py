
from sqlalchemy import select
from sqlalchemy.orm import Session

from App.Modules.Authentication.models import (
    Permission,
    role_permissions,
    User
)


def user_has_permission(
    db: Session,
    user: User,
    permission_name: str
) -> bool:

    statement = (
        select(Permission.permission_id)
        .join(
            role_permissions,
            Permission.permission_id
            == role_permissions.c.permission_id
        )
        .where(
            Permission.permission_name == permission_name,
            role_permissions.c.role_id == user.role_id
        )
        .limit(1)
    )

    result = db.execute(statement).scalar_one_or_none()

    return result is not None