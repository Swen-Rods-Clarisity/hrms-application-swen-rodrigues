from datetime import datetime, timezone, timedelta

import jwt
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash

from App.Core.config import settings


# Password Hashing

password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(
    password: str,
    hashed_password: str
) -> bool:
    return password_hash.verify(
        password,
        hashed_password
    )


# JWT Authentication

def create_access_token(
    data: dict,
    expires_delta: timedelta | None = None
) -> str:

    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.jwt_access_token_expire_minutes
        )

    to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(
        to_encode,
        settings.jwt_secret_key,
        algorithm=settings.jwt_algorithm
    )

    return encoded_jwt


def decode_access_token(token: str):
    try:
        payload = jwt.decode(
            token,
            settings.jwt_secret_key,
            algorithms=[settings.jwt_algorithm]
        )

        return payload

    except InvalidTokenError as error:
        print("JWT DECODE ERROR:", type(error).__name__, str(error))
        return None