from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel

from app.models.message import Message
from app.models.threadMember import ThreadMember


class Thread(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime
    updated_at: datetime

    members: list[ThreadMember] | None = Relationship(back_populates="thread")
    messages: list[Message] = Relationship(back_populates="thread")
