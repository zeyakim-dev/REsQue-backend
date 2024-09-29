from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

from app.domains.project.value_objects import ProjectMemberRole
from app.shared.domains.entities.base_entity import BaseEntity
from app.shared.domains.mixins.soft_deletion_mixin import SoftDeletionMixin
from app.shared.domains.mixins.timestamp_mixin import TimestampMixin


@dataclass(kw_only=True, frozen=True)
class ProjectMember(BaseEntity, TimestampMixin, SoftDeletionMixin):
    project_id: int
    user_id: int
    role: ProjectMemberRole
    joined_at: datetime = field(default_factory=datetime.now)
    last_access_at: Optional[datetime] = None
