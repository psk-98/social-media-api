from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel

from app.models.thread import Thread
from app.models.user import User


class ThreadMember(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    last_read_message_id: int | None = Field(default=None)
    joined_at: datetime
    left_at: datetime | None = Field(default=None)

    user_id: int | None = Field(default=None, foreign_key="users.id")
    user: User | None = Relationship()
    thread: Thread = Relationship(back_populates="members")
