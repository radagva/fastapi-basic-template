from typing import List
from fastapi import APIRouter, Depends
from app.config.database import Session, get_database
from app.core.dto.users import User
from app.core.models import UserModel
from app.utils.security import auth_required

router = APIRouter(prefix="/users")


@router.get("")
def index(
    database: Session = Depends(get_database), _=Depends(auth_required)
) -> List[User]:
    users = database.query(UserModel).all()
    return [user for user in users]
