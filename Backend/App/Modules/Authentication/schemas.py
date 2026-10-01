from datetime import datetime

from pydantic import BaseModel, Field


class SignUpRequest(BaseModel):
    username: str = Field(..., min_length=1, max_length=50)
    password: str = Field(..., min_length=1)


class LoginRequest(BaseModel):
    username: str = Field(..., min_length=1, max_length=50)
    password: str = Field(..., min_length=1)


class UserResponse(BaseModel):
    user_id: int
    username: str
    created_at: datetime

    class Config:
        from_attributes = True


class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    must_change_password: bool 
    


class ResetPasswordRequest(BaseModel):
    username: str = Field(..., min_length=1, max_length=50)
    new_password: str = Field(..., min_length=1)


class TokenDate(BaseModel):
    user_id: int

class ChangePasswordRequest(BaseModel):
    current_password: str = Field(
        ...,
        min_length=1
    )

    new_password: str = Field(
        ...,
        min_length=1
    )