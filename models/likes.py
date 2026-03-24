from enum import Enum as PyEnum

from sqlalchemy import Column, Enum, ForeignKey, Integer, UniqueConstraint

from models.base import Base
from models.mixins import TimestampMixin


class LikedType(str, PyEnum):
    post = "post"


class Like(TimestampMixin, Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    liked_id = Column(Integer, nullable=False, index=True)
    liked_type = Column(Enum(LikedType), nullable=False)

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "liked_id",
            "liked_type",
            name="unqiue_user_like",
        ),
    )
