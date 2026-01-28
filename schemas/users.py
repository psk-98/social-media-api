from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    email: str
    username: str
    password: str
    is_active: bool
    role: str


class UpdateUserRequest(BaseModel):
    email: str
    username: str
    password: str
    is_active: bool
    role: str
