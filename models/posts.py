from sqlalchemy import Column, ForeignKey, Integer, String, and_
from sqlalchemy.orm import Mapped, foreign, relationship

from models.base import Base
from models.mixins import TimestampMixin


class Post(TimestampMixin, Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    # many posts belong to one user
    # user: Mapped["User"] = relationship(
    #     "User",
    #     back_populates="posts",
    # )

    # likes = relationship(
    #     "Like",
    #     primaryjoin=lambda: and_(
    #         foreign(Like.liked_id) == Post.id,
    #         Like.liked_type == "Post",
    #     ),
    #     viewonly=True,
    # )
