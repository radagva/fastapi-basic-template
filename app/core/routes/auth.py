from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.dto.auth import LoginDTO, RegisterDTO
from app.core.dto.users import User
from app.utils.security import (
    auth_required,
    hash_password,
    verify_password,
    create_access_token,
)
from app.config.database import get_database
from app.core.models import UserModel

router = APIRouter(prefix="/auth")


@router.post("/login")
def login(input: LoginDTO, database: Session = Depends(get_database)):
    if user := database.query(UserModel).filter(UserModel.email == input.email).first():
        if verify_password(input.password, str(user.password)):
            token = create_access_token(
                {"id": user.id}, expires_delta=timedelta(days=14)
            )

            return {"access_token": token}

    raise HTTPException(status_code=401, detail="Unable to login")


@router.post("/register")
def register(input: RegisterDTO, database: Session = Depends(get_database)):
    user = UserModel(**input.model_dump())
    user.password = hash_password(input.password)
    database.add(user)
    database.commit()
    database.refresh(user)
    return user


@router.get("/me")
def me(user: UserModel = Depends(auth_required)) -> User:
    return user
