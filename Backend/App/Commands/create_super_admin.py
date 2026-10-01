import getpass

from sqlalchemy import select

from App.Core.database import SessionLocal
from App.Core.security import hash_password
from App.Modules.Authentication.models import User, Role


def create_super_admin():

    username = input("Enter Super Admin username: ").strip()
    password = getpass.getpass("Enter Super Admin password: ")

    db = SessionLocal()

    try:

        # Check if username already exists
        existing_user = db.execute(
            select(User).where(
                User.username == username
            )
        ).scalar_one_or_none()

        if existing_user:
            print("A user with this username already exists.")
            return

        # Find the existing Super Admin role
        super_admin_role = db.execute(
            select(Role).where(
                Role.role_name == "Super Admin"
            )
        ).scalar_one_or_none()

        if super_admin_role is None:
            print("Super Admin role does not exist.")
            print("Run seed_rbac.py first.")
            return

        # Hash the password
        hashed_password = hash_password(password)

        # Create Super Admin user
        super_admin = User(
            username=username,
            password_hash=hashed_password,
            role_id=super_admin_role.role_id
        )

        db.add(super_admin)

        db.commit()

        db.refresh(super_admin)

        print(
            f"Super Admin '{super_admin.username}' "
            "created successfully."
        )

    except Exception as e:

        db.rollback()

        print(f"Failed to create Super Admin: {e}")

    finally:

        db.close()


if __name__ == "__main__":
    create_super_admin()