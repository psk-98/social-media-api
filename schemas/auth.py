from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    email: str
    username: str
    password: str
    is_active: bool
    role: str


class CurrentUser(BaseModel):
    user: str


# class LoginResponse(BaseModel):
#     user_id: int
