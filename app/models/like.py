from sqlmodel import Field, Relationship, SQLModel

from app.models.comment import Comment
from app.models.post import Post
from app.models.user import User


class Like(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    user_id: int | None = Field(default=None, foreign_key="users.id")
    user: User | None = Relationship(back_populates="likes")
    comment_id: int | None = Field(default=None, foreign_key="comments.id", index=True)
    comment: Comment | None = Relationship(back_populates="comment")
    post_id: int | None = Field(default=None, foreign_key="posts.id", index=True)
    post: Post | None = Relationship(back_populates="post")
