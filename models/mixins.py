from datetime import datetime

from pydantic import Field


class TimestampMixin:
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
