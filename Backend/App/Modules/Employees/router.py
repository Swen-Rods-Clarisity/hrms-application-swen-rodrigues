from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from App.Core.database import get_db
from App.Core.dependencies import get_current_user_with_password_check
from App.Modules.Authentication.models import User
from App.Modules.Employees.schemas import (
    EmployeeOnboardingRequest,
    EmployeeResponse
)
from App.Modules.Employees.service import onboard_employee


router = APIRouter(
    prefix="/api/v1/employees",
    tags=["Employees"]
)


@router.post(
    "/onboard",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED
)
def onboard_employee_api(
    data: EmployeeOnboardingRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user_with_password_check
    )
):
    employee, result = onboard_employee(
        db=db,
        current_user=current_user,
        data=data
    )

    if employee is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=result
        )

    return employee