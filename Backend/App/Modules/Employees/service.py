from uuid import uuid4

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from App.Core.permissions import user_has_permission
from App.Core.security import hash_password

from App.Modules.Authentication.models import (
    Role,
    User
)

from App.common.constants.roles import (
    SUPER_ADMIN,
    HR,
    EMPLOYEE,
    MANAGER
)

from App.Modules.Employees.models import Employee
from App.Modules.Employees.schemas import EmployeeOnboardingRequest


def onboard_employee(
    db: Session,
    current_user: User,
    data: EmployeeOnboardingRequest
):
    # ---------------------------------------------------------
    # 1. Check permission
    # ---------------------------------------------------------

    if not user_has_permission(
        db,
        current_user,
        "user:create"
    ):
        return None, "You do not have permission to create users"

    # ---------------------------------------------------------
    # 2. Find requested role by role name
    # ---------------------------------------------------------

    role = db.execute(
        select(Role).where(
            Role.role_name == data.role_name
        )
    ).scalar_one_or_none()

    if role is None:
        return None, "Invalid role name"

    # ---------------------------------------------------------
    # 3. Check whether current user is allowed
    #    to assign this role
    # ---------------------------------------------------------

    if current_user.role.role_name == SUPER_ADMIN:

        allowed_roles = {
            HR,
            MANAGER,
            EMPLOYEE
        }

    elif current_user.role.role_name == HR:

        allowed_roles = {
            MANAGER,
            EMPLOYEE
        }

    else:

        allowed_roles = set()

    if role.role_name not in allowed_roles:

        return (
            None,
            f"{current_user.role.role_name} cannot assign the "
            f"{role.role_name} role"
        )

    # ---------------------------------------------------------
    # 4. Check employee email
    # ---------------------------------------------------------

    existing_employee = db.execute(
        select(Employee).where(
            Employee.email == data.email
        )
    ).scalar_one_or_none()

    if existing_employee:

        return (
            None,
            "An employee with this email already exists"
        )

    # ---------------------------------------------------------
    # 5. Check username
    #
    # Username will be the employee email.
    # ---------------------------------------------------------

    existing_user = db.execute(
        select(User).where(
            User.username == data.email
        )
    ).scalar_one_or_none()

    if existing_user:

        return (
            None,
            "A user with this email already exists"
        )

    # ---------------------------------------------------------
    # 6. Generate temporary employee code
    # ---------------------------------------------------------

    temporary_employee_code = (
        f"T{uuid4().hex[:18]}"
    )

    # ---------------------------------------------------------
    # 7. Create employee
    # ---------------------------------------------------------

    employee = Employee(
        employee_code=temporary_employee_code,
        first_name=data.first_name,
        last_name=data.last_name,
        email=data.email,
        phone=data.phone,
        dob=data.dob,
        date_of_joining=data.date_of_joining,
        employment_type=data.employment_type
    )

    db.add(employee)

    db.flush()

    # ---------------------------------------------------------
    # 8. Generate final employee code
    #
    # Example:
    # employee_id = 27
    # employee_code = EMP000027
    # ---------------------------------------------------------

    employee.employee_code = (
        f"EMP{employee.employee_id:06d}"
    )

    # ---------------------------------------------------------
    # 9. Create user account
    # ---------------------------------------------------------

    user = User(
        employee_id=employee.employee_id,
        role_id=role.role_id,
        username=data.email,
        password_hash=hash_password(
            data.initial_password
        ),
        is_active=True,
        must_change_password=True
    )

    db.add(user)

    # ---------------------------------------------------------
    # 10. Commit employee + user together
    # ---------------------------------------------------------

    try:

        db.commit()

    except IntegrityError:

        db.rollback()

        return (
            None,
            "Employee or user could not be created"
        )

    # ---------------------------------------------------------
    # 11. Refresh records
    # ---------------------------------------------------------

    db.refresh(employee)
    db.refresh(user)

    return employee, user