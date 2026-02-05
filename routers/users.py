from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext
from starlette import status

from core.dependencies import db_dependency, user_dependency
from models.users import User
from schemas.users import ChangeUserPasswordRequest, UserResponse

router = APIRouter(prefix="/users", tags=["users"])

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.get("/", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def get_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Auth failed")

    return db.query(User).filter(User.id == user.get("user_id")).first()


@router.put("/change_password", status_code=status.HTTP_202_ACCEPTED)
async def change_password(
    user: user_dependency, db: db_dependency, request: ChangeUserPasswordRequest
):
    if user is None:
        raise HTTPException(status_code=401, detail="Auth failed")

    user_instance = db.query(User).filter(User.id == user.get("user_id")).first()

    if not bcrypt_context.verify(request.password, user_instance.password):
        raise HTTPException(status_code=401, detail="Error on password change")

    user_instance.password = bcrypt_context.hash(request.password)
    db.commit()
