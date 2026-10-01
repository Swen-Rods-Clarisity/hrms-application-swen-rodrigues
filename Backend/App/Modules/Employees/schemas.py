from datetime import date, datetime

from pydantic import BaseModel, Field


class EmployeeOnboardingRequest(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    last_name: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    email: str = Field(
        ...,
        min_length=1,
        max_length=255
    )

    phone: str | None = Field(
        default=None,
        max_length=20
    )

    dob: date | None = None

    date_of_joining: date

    employment_type: str = Field(
        ...,
        min_length=1,
        max_length=50
    )

    role_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )

    initial_password: str = Field(
        ...,
        min_length=1
    )


class EmployeeResponse(BaseModel):
    employee_id: int
    employee_code: str
    first_name: str
    last_name: str
    email: str
    phone: str | None
    dob: date | None
    date_of_joining: date
    employment_type: str
    status: str
    department_id: int | None
    designation_id: int | None
    manager_id: int | None
    residential_address_id: int | None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True