from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint

from models.base import Base
from models.mixins import TimestampMixin


class Follow(TimestampMixin, Base):
    __tablename__ = "follows"

    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    followed_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    __table_args__ = (
        UniqueConstraint(
            "follower_id",
            "followed_id",
            name="unique_follow",
        ),
    )
