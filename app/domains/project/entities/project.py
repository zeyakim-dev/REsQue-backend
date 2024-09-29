from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

from app.shared.domains.entities.base_entity import BaseEntity
from app.shared.domains.mixins.soft_deletion_mixin import SoftDeletionMixin
from app.shared.domains.mixins.timestamp_mixin import TimestampMixin


@dataclass(kw_only=True, frozen=True)
class Project(BaseEntity, TimestampMixin, SoftDeletionMixin):
    name: str
    description: str
    founder_id: int
    members: List[int] = field(default_factory=list)
