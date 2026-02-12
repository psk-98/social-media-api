from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import Mapped, relationship

from models.base import Base
from models.mixins import TimestampMixin


class User(TimestampMixin, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)

    # one user has many posts
    posts: Mapped[list["Post"]] = relationship(
        "Post",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    likes: Mapped[list["Like"]] = relationship("Like")
