from pydantic import BaseModel


class LikeRequest(BaseModel):
    user_id: str
    liked_id: str
    liked_type: str

    model_config = {"from_attributes": True}
