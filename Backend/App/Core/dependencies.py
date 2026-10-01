from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy import select
from sqlalchemy.orm import Session

from App.Core.database import get_db
from App.Core.security import decode_access_token
from App.Modules.Authentication.models import User


security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):

    token = credentials.credentials

    payload = decode_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={
                "WWW-Authenticate": "Bearer"
            }
        )

    user_id = payload.get("sub")

    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={
                "WWW-Authenticate": "Bearer"
            }
        )

    try:
        user_id = int(user_id)

    except (TypeError, ValueError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={
                "WWW-Authenticate": "Bearer"
            }
        )

    user = db.execute(
        select(User).where(
            User.user_id == user_id
        )
    ).scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={
                "WWW-Authenticate": "Bearer"
            }
        )

    return user

def get_current_user_with_password_check(
    current_user: User = Depends(get_current_user)
):
    if current_user.must_change_password:

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Password change required"
        )

    return current_user