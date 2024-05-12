from pydantic import UUID4
from sqlalchemy import UUID, ForeignKey, String, DateTime, func
from datetime import datetime
import uuid

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.config.database import Base


class UserModel(Base):
    __tablename__ = "users"
    id: Mapped[UUID4] = mapped_column(
        UUID, index=True, primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now(), onupdate=datetime.now
    )

    confessions = relationship("ConfessionModel", back_populates="user")


class ConfessionModel(Base):
    __tablename__ = "confessions"

    id: Mapped[UUID4] = mapped_column(
        UUID, index=True, primary_key=True, default=uuid.uuid4
    )
    title: Mapped[str | None] = mapped_column(String, nullable=True)
    content: Mapped[str] = mapped_column(String)
    user_id: Mapped[UUID4] = mapped_column(UUID, ForeignKey("users.id"))
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now(), onupdate=datetime.now
    )

    user = relationship("UserModel", back_populates="confessions")
