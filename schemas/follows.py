from pydantic import BaseModel


class Follow(BaseModel):
    followed: str
