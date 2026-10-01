from sqlalchemy import select

from App.Core.database import SessionLocal
from App.Modules.Authentication.models import Role, Permission


ROLES = [
    {
        "role_name": "Super Admin",
        "description": "Full system administration access",
    },
    {
        "role_name": "HR",
        "description": "Human resources administration access",
    },
    {
        "role_name": "Employee",
        "description": "Standard employee access",
    },
    {
        "role_name": "Manager",
        "description": "Manager responsible for assigned employees and team activities",
    },
]


PERMISSIONS = [
    {
        "permission_name": "user:create",
        "module": "authentication",
        "description": "Create users",
    },
    {
        "permission_name": "user:read",
        "module": "authentication",
        "description": "View users",
    },
    {
        "permission_name": "user:update",
        "module": "authentication",
        "description": "Update users",
    },
    {
        "permission_name": "user:delete",
        "module": "authentication",
        "description": "Delete users",
    },
    {
        "permission_name": "user:activate",
        "module": "authentication",
        "description": "Activate users",
    },
    {
        "permission_name": "user:deactivate",
        "module": "authentication",
        "description": "Deactivate users",
    },
    {
        "permission_name": "role:create",
        "module": "authentication",
        "description": "Create roles",
    },
    {
        "permission_name": "role:read",
        "module": "authentication",
        "description": "View roles",
    },
    {
        "permission_name": "role:update",
        "module": "authentication",
        "description": "Update roles",
    },
    {
        "permission_name": "role:delete",
        "module": "authentication",
        "description": "Delete roles",
    },
    {
        "permission_name": "role:assign",
        "module": "authentication",
        "description": "Assign roles to users",
    },
    {
        "permission_name": "permission:read",
        "module": "authentication",
        "description": "View permissions",
    },
]


ROLE_PERMISSIONS = {
    "Super Admin": [
        "user:create",
        "user:read",
        "user:update",
        "user:delete",
        "user:activate",
        "user:deactivate",
        "role:create",
        "role:read",
        "role:update",
        "role:delete",
        "role:assign",
        "permission:read",
    ],

    "HR": [
        "user:create",
        "user:read",
        "user:update",
        "user:activate",
        "user:deactivate",
        "role:read",
    ],

    "Employee": [],

    "Manager": [],
}


def seed_rbac():

    db = SessionLocal()

    try:

        # ---------------------------------------------------------
        # Create roles
        # ---------------------------------------------------------

        for role_data in ROLES:

            existing_role = db.execute(
                select(Role).where(
                    Role.role_name == role_data["role_name"]
                )
            ).scalar_one_or_none()

            if existing_role is None:

                db.add(
                    Role(**role_data)
                )

        db.flush()

        # ---------------------------------------------------------
        # Create permissions
        # ---------------------------------------------------------

        for permission_data in PERMISSIONS:

            existing_permission = db.execute(
                select(Permission).where(
                    Permission.permission_name
                    == permission_data["permission_name"]
                )
            ).scalar_one_or_none()

            if existing_permission is None:

                db.add(
                    Permission(**permission_data)
                )

        db.flush()

        # ---------------------------------------------------------
        # Assign permissions to roles
        # ---------------------------------------------------------

        for role_name, permission_names in ROLE_PERMISSIONS.items():

            role = db.execute(
                select(Role).where(
                    Role.role_name == role_name
                )
            ).scalar_one()

            for permission_name in permission_names:

                permission = db.execute(
                    select(Permission).where(
                        Permission.permission_name
                        == permission_name
                    )
                ).scalar_one()

                if permission not in role.permissions:

                    role.permissions.append(
                        permission
                    )

        # ---------------------------------------------------------
        # Commit all RBAC changes
        # ---------------------------------------------------------

        db.commit()

        print(
            "RBAC data seeded successfully."
        )

    except Exception:

        db.rollback()

        raise

    finally:

        db.close()


if __name__ == "__main__":
    seed_rbac()