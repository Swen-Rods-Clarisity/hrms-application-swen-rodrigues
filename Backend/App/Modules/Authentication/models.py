from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from App.Core.database import Base


role_permissions = Table(
    "role_permissions",
    Base.metadata,
    Column(
        "role_id",
        ForeignKey("roles.role_id"),
        primary_key=True
    ),
    Column(
        "permission_id",
        ForeignKey("permissions.permission_id"),
        primary_key=True
    )
)


class Role(Base):
    __tablename__ = "roles"

    role_id: Mapped[int] = mapped_column(
        primary_key=True
    )

    role_name: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        String(255),
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

    users: Mapped[list["User"]] = relationship(
        back_populates="role"
    )

    permissions: Mapped[list["Permission"]] = relationship(
        secondary=role_permissions,
        back_populates="roles"
    )


class Permission(Base):
    __tablename__ = "permissions"

    permission_id: Mapped[int] = mapped_column(
        primary_key=True
    )

    permission_name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    module: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    roles: Mapped[list["Role"]] = relationship(
        secondary=role_permissions,
        back_populates="permissions"
    )


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(
        primary_key=True
    )

    employee_id: Mapped[int | None] = mapped_column(
    ForeignKey("employees.employee_id"),
    nullable=True,
    unique=True
)

    role_id: Mapped[int] = mapped_column(
        ForeignKey("roles.role_id"),
        nullable=False
    )

    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    must_change_password: Mapped[bool] = mapped_column(
    Boolean,
    default=True,
    nullable=False
    )

    last_login: Mapped[datetime | None] = mapped_column(
        DateTime,
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

    role: Mapped["Role"] = relationship(
        back_populates="users"
    )   