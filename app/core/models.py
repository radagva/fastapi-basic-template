import uuid
from pydantic import UUID4
from sqlalchemy import UUID, String, DateTime, func
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column

from app.config.database import Base


class Model(Base):
    __abstract__ = True
    id: Mapped[UUID4] = mapped_column(
        UUID, index=True, primary_key=True, default=uuid.uuid4
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, server_default=func.now(), onupdate=datetime.now
    )


class UserModel(Model):
    __tablename__ = "users"
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
