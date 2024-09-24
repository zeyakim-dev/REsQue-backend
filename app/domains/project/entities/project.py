from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

from app.shared.domain.base_entity import BaseEntity
from app.shared.domain.mixin.soft_deletion_mixin import SoftDeletionMixin
from app.shared.domain.mixin.timestamp_mixin import TimestampMixin


@dataclass(kw_only=True)
class Project(BaseEntity, TimestampMixin, SoftDeletionMixin):
    name: str
    description: str
    founder_id: int
    members: List[int] = field(default_factory=list)
