from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from App.Core.database import get_db
from App.Core.dependencies import get_current_user

from App.Modules.Authentication.models import User

from App.Modules.Authentication.schemas import (
    LoginRequest,
    SignUpRequest,
    LoginResponse,
    UserResponse,
    ResetPasswordRequest,
)

from App.Modules.Authentication.service import (
    create_user,
    authenticate_user,
    show_user,
    create_user_access_token,
    reset_password,
)

from App.Modules.Authentication.schemas import (
    ChangePasswordRequest
)

from App.Modules.Authentication.service import (
    change_password
)

from App.Core.dependencies import get_current_user_with_password_check


router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)


@router.post(
    "/signup",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def signup(
    data: SignUpRequest,
    db: Session = Depends(get_db)
):

    try:

        user = create_user(
            db=db,
            data=data
        )

    except ValueError as error:

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error)
        )

    return user


@router.post(
    "/login",
    response_model=LoginResponse
)
def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):

    user = authenticate_user(
        db=db,
        username=data.username,
        password=data.password
    )

    if user is None:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={
                "WWW-Authenticate": "Bearer"
            }
        )

    access_token = create_user_access_token(user)

    return LoginResponse(
    access_token=access_token,
    token_type="bearer",
    must_change_password=user.must_change_password
    )


@router.get(
    "/users",
    response_model=list[UserResponse]
)
def get_all_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return show_user(db)


@router.get("/me")
def get_me(
    current_user: User = Depends(
        get_current_user_with_password_check
    )
):
    return current_user


@router.post(
    "/reset-password",
    response_model=UserResponse
)
def reset_user_password(
    data: ResetPasswordRequest,
    db: Session = Depends(get_db)
):

    user = reset_password(
        db=db,
        username=data.username,
        new_password=data.new_password
    )

    if user is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user

@router.post(
    "/change-password",
    status_code=status.HTTP_200_OK
)
def change_password_api(
    data: ChangePasswordRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    success = change_password(
        db=db,
        user=current_user,
        current_password=data.current_password,
        new_password=data.new_password
    )

    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Current password is incorrect"
        )

    return {
        "message": "Password changed successfully"
    }