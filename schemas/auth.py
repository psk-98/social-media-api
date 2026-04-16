from enum import Enum as PyEnum

from pydantic import BaseModel, EmailStr


class UserRole(str, PyEnum):
    user = "user"
    admin = "admin"


class CreateUserRequest(BaseModel):
    email: EmailStr
    username: str
    password: str
    is_active: bool
    role: UserRole


class CurrentUser(BaseModel):
    user: str


# class LoginResponse(BaseModel):
#     user_id: int
