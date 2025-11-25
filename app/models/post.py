from sqlmodel import Field, Relationship, SQLModel

from app.models.comment import Comment
from app.models.like import Like
from app.models.mixins import TimestampMixin
from app.models.user import User


class Post(TimestampMixin, SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    content: str

    user_id: int | None = Field(default=None, foreign_key="users.id")
    user: User | None = Relationship(back_populates="user")
    comments: list[Comment] = Relationship(back_populates="post")
    likes: list[Like] = Relationship(back_populates="post")
