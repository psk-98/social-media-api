from sqlmodel import Field, Relationship, SQLModel

from app.models.mixins import TimestampMixin
from app.models.user import User


class Notification(TimestampMixin, SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    is_seen: bool = Field(default=False)
    content: str
    type: str

    thread_id: int | None = Field(default=None, foreign_key="threads.id")
    message_id: int | None = Field(default=None, foreign_key="messages.id")
    post_id: int | None = Field(default=None, foreign_key="posts.id")

    receiver_id: int = Field(foreign_key="users.id", index=True)
    receiver: User = Relationship(
        sa_relationship_kwargs={"foreign_keys": "[Notification.receiver_id]"}
    )
    actor_id: int = Field(foreign_key="users.id")
    actor: User = Relationship(
        sa_relationship_kwargs={"foreign_keys": "[Notification.actor_id]"}
    )
