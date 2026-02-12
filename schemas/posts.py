from typing import List

from pydantic import BaseModel

from schemas.likes import LikeRequest


class CreatePostRequest(BaseModel):
    content: str


class UpdatePostRequest(BaseModel):
    content: str


class PostResponse(BaseModel):
    id: int
    content: str
    user_id: int
    likes: List[LikeRequest]

    model_config = {"from_attributes": True}
