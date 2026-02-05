from pydantic import BaseModel


class CreatePostRequest(BaseModel):
    content: str


class UpdatePostRequest(BaseModel):
    content: str


class PostRespoonse(BaseModel):
    id: int
    content: str
    user_id: int

    model_config = {"from_attributes": True}
