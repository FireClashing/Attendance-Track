

import enum

from sqlalchemy import (
    BigInteger,
    Boolean,
    Date,
    DateTime,
    Enum,
    ForeignKey,
    Index,
    String,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


# --------------------------------------------------
# ENUMS
# --------------------------------------------------

class UserRole(str, enum.Enum):
    STUDENT = "student"
    TEACHER = "teacher"


class AttendanceStatus(str, enum.Enum):
    PRESENT = "present"
    ABSENT = "absent"


# --------------------------------------------------
# USERS TABLE
# --------------------------------------------------

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        BigInteger(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    full_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
        index=False,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole, name="user_role"),
        nullable=False,
    )

    roll_number: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
        unique=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
        server_default="1",
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.current_timestamp(),
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
    )

    # Relationships
    attendance_records: Mapped[list["Attendance"]] = relationship(
        back_populates="student",
        foreign_keys="Attendance.student_id",
    )

    marked_attendance: Mapped[list["Attendance"]] = relationship(
        back_populates="teacher",
        foreign_keys="Attendance.marked_by",
    )


# --------------------------------------------------
# ATTENDANCE TABLE
# --------------------------------------------------

class Attendance(Base):
    __tablename__ = "attendance"

    __table_args__ = (
        UniqueConstraint(
            "student_id",
            "attendance_date",
            name="uq_student_attendance_date",
        ),
        Index(
            "idx_attendance_date",
            "attendance_date",
        ),
        Index(
            "idx_attendance_teacher_date",
            "marked_by",
            "attendance_date",
        ),
    )

    id: Mapped[int] = mapped_column(
        BigInteger(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    student_id: Mapped[int] = mapped_column(
        BigInteger(unsigned=True),
        ForeignKey("users.id", ondelete="RESTRICT"),
        nullable=False,
    )

    attendance_date: Mapped[Date] = mapped_column(
        Date,
        nullable=False,
    )

    status: Mapped[AttendanceStatus] = mapped_column(
        Enum(AttendanceStatus, name="attendance_status"),
        nullable=False,
    )

    marked_by: Mapped[int] = mapped_column(
        BigInteger(unsigned=True),
        ForeignKey("users.id", ondelete="RESTRICT"),
        nullable=False,
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.current_timestamp(),
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
    )

    # Relationships
    student: Mapped["User"] = relationship(
        back_populates="attendance_records",
        foreign_keys=[student_id],
    )

    teacher: Mapped["User"] = relationship(
        back_populates="marked_attendance",
        foreign_keys=[marked_by],
    )
