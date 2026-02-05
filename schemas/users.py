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


class UserResponse(BaseModel):
    email: str
    username: str
    role: str

    model_config = {"from_attributes": True}
