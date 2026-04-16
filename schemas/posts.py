from typing import List

from pydantic import BaseModel, ConfigDict

from schemas.likes import LikeRequest


class CreatePostRequest(BaseModel):
    content: str

    model_config = {"json_schema_extra": {"example": {"content": "the post content"}}}


class UpdatePostRequest(BaseModel):
    content: str

    model_config = {"json_schema_extra": {"example": {"content": "the post content"}}}


class PostResponse(BaseModel):
    id: int
    content: str
    user_id: int
    # likes: List[LikeRequest]

    # model_config = {"from_attributes": True}
