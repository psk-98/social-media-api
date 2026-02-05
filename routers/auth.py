from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette import status

from core.dependencies import db_dependency
from core.jwt import create_access_token
from core.security import hash_password, verify_password
from core.settings import get_settings
from models import User
from schemas.auth import CreateUserRequest
from schemas.users import UserResponse

router = APIRouter(prefix="/auth", tags=["auth"])

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

settings = get_settings()


def authenticate_user(username: str, password: str, db):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


@router.get("/", status_code=status.HTTP_200_OK)
def users(db: db_dependency):
    return db.query(User).all()


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(request: CreateUserRequest, db: db_dependency):
    request_data = request.model_dump()
    request_data["password"] = hash_password(request.password)
    create_user_model = User(**request_data)
    db.add(create_user_model)
    db.commit()

    return create_user_model


@router.post("/token", status_code=status.HTTP_200_OK)
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user"
        )
    token = create_access_token(
        user.username, user.id, user.role, timedelta(minutes=20)
    )

    return {"access_token": token, "token_type": "Bearer"}
