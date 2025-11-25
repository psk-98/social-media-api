from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel

from app.models.thread import Thread
from app.models.user import User


class Message(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    content: str
    is_seen: bool
    created_at: datetime
    updated_at: datetime

    sender_id: int | None = Field(default=None, foreign_key="user.id")
    sender: User | None = Relationship()
    thread_id: int | None = Field(default=None, foreign_key="threads.id", index=True)
    thread: Thread = Relationship(back_populates="messages")
