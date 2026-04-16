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

    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "user@example.com",
                "username": "johndoe",
                "password": "stongpassword123",
                "role": "user",
            }
        }
    }


class CurrentUser(BaseModel):
    user: str


# class LoginResponse(BaseModel):
#     user_id: int
