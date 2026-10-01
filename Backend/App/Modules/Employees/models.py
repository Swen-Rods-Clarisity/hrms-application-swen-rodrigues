from datetime import date, datetime

from sqlalchemy import Date, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from App.Core.database import Base


class Employee(Base):
    __tablename__ = "employees"

    employee_id: Mapped[int] = mapped_column(
        primary_key=True
    )

    employee_code: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False
    )

    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    last_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    phone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    dob: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    date_of_joining: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    employment_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="Active",
        nullable=False
    )

    department_id: Mapped[int | None] = mapped_column(
        nullable=True
    )

    designation_id: Mapped[int | None] = mapped_column(
        nullable=True
    )

    manager_id: Mapped[int | None] = mapped_column(
        nullable=True
    )

    residential_address_id: Mapped[int | None] = mapped_column(
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )