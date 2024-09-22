from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

from app.shared.domain.base_entity import BaseEntity
from app.shared.domain.mixin.soft_deletion_mixin import SoftDeletionMixin
from app.shared.domain.mixin.timestamp_mixin import TimestampMixin
from app.domains.project.value_objects import ProjectMemberRole

@dataclass(kw_only=True)
class ProjectMember(BaseEntity, TimestampMixin, SoftDeletionMixin):
    project_id: int
    user_id: int
    role: ProjectMemberRole
    joined_at: datetime = field(default_factory=datetime.now)
    last_access_at: Optional[datetime] = None