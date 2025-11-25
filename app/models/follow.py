from sqlmodel import Field, Relationship, SQLModel

from app.models.mixins import TimestampMixin
from app.models.user import User


class Follow(TimestampMixin, SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    follower_id: int = Field(foreign_key="users.id", index=True)
    follower: User = Relationship(
        sa_relationship_kwargs={"foreign_keys": "[Follow.follower_id]"}
    )
    followed_id: int = Field(foreign_key="users.id", index=True)

    followed: User = Relationship(
        sa_relationship_kwargs={"foreign_keys": "[Follow.followed_id]"}
    )
