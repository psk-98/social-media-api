from sqlmodel import Field, Relationship, SQLModel

from app.models.like import Like
from app.models.mixins import TimestampMixin
from app.models.post import Post
from app.models.user import User


class Comment(TimestampMixin, SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    content: str

    user_id: int | None = Field(default=None, foreign_key="users.id")
    user: User | None = Relationship(back_populates="user")
    post_id: int | None = Field(default=None, foreign_key="posts.id", index=True)
    post: Post | None = Relationship(back_populates="post")
    likes: list[Like] = Relationship(back_populates="comment")
