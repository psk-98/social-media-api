from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship

from models.base import Base
from models.mixins import TimestampMixin


class Post(TimestampMixin, Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    # many posts belong to one user
    user: Mapped["User"] = relationship(
        "User",
        back_populates="posts",
    )
