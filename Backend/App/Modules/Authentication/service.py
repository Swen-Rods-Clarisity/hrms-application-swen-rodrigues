from sqlalchemy import select
from sqlalchemy.orm import Session

from App.Core.security import (
    hash_password,
    verify_password,
    create_access_token
)
from App.Modules.Authentication.models import User
from App.Modules.Authentication.schemas import SignUpRequest


def create_user(db: Session, data: SignUpRequest):

    existing_user = db.execute(
        select(User).where(
            User.username == data.username
        )
    ).scalar_one_or_none()

    if existing_user:
        return None

    user = User(
        username=data.username,
        password_hash=hash_password(data.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def authenticate_user(
    db: Session,
    username: str,
    password: str
):

    user = db.execute(
        select(User).where(
            User.username == username
        )
    ).scalar_one_or_none()

    if user is None:
        return None

    if not user.is_active:
        return None

    if not verify_password(
        password,
        user.password_hash
    ):
        return None

    return user


def show_user(db: Session):

    users = db.execute(
        select(User)
    ).scalars().all()

    return users

def create_user_access_token(user: User) -> str:

    access_token = create_access_token(
        data={
            "sub": str(user.user_id),
            "role": user.role.role_name,
            "must_change_password": user.must_change_password
        }
    )

    return access_token

def reset_password(
    db: Session,
    username: str,
    new_password: str
):

    user = db.execute(
        select(User).where(
            User.username == username
        )
    ).scalar_one_or_none()

    if user is None:
        return None

    user.password_hash = hash_password(new_password)

    db.commit()
    db.refresh(user)

    return user

def change_password(
    db: Session,
    user: User,
    current_password: str,
    new_password: str
):

    if not verify_password(
        current_password,
        user.password_hash
    ):
        return False

    user.password_hash = hash_password(
        new_password
    )

    user.must_change_password = False

    db.commit()
    db.refresh(user)

    return True