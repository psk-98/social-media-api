from sqlmodel import Field, Relationship, SQLModel

from app.models.comment import Comment
from app.models.like import Like
from app.models.mixins import TimestampMixin
from app.models.post import Post


class User(TimestampMixin, SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    posts: list[Post] = Relationship(back_populates="user")
    comments: list[Comment] = Relationship(back_populates="user")
    likes: list[Like] = Relationship(back_populates="user")
