from datetime import datetime
from pydantic import UUID4, BaseModel


class User(BaseModel):
    id: UUID4
    name: str
    email: str
    created_at: datetime
    updated_at: datetime
