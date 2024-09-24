from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class SoftDeletionMixin:
    is_deleted: bool = False
    deleted_at: Optional[datetime] = None
