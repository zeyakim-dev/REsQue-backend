from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class TimestampMixin:
    created_at: datetime = field(default_factory=datetime.now, init=False, repr=True)
    updated_at: datetime = field(default_factory=datetime.now)
