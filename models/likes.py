from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint

from models.base import Base
from models.mixins import TimestampMixin


class Like(TimestampMixin, Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    liked_id = Column(Integer)
    liked_type = Column(String)

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "liked_id",
            "liked_type",
            name="unqiue_user_like",
        ),
    )
