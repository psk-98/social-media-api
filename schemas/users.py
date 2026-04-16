from pydantic import BaseModel, Field


class UpdateUserRequest(BaseModel):
    email: str
    username: str
    password: str
    is_active: bool
    role: str


class ChangeUserPasswordRequest(BaseModel):
    password: str
    new_password: str = Field(min_length=8)

    model_config = {
        "json_schema_extra": {
            "example": {"password": "oldpassword", "new_password": "newpassword"}
        }
    }


class UserResponse(BaseModel):
    email: str
    username: str
    role: str

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {
                "email": "user@example.com",
                "username": "johndoe",
                "role": "user",
            }
        },
    }
