from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from app.domains.requirement.value_objects import (
    RequirementComplexity,
    RequirementPriority,
    RequirementStatus,
    RequirementType,
)
from app.shared.domain.base_entity import BaseEntity
from app.shared.domain.mixin.soft_deletion_mixin import SoftDeletionMixin
from app.shared.domain.mixin.timestamp_mixin import TimestampMixin


@dataclass
class Requirement(BaseEntity, TimestampMixin, SoftDeletionMixin):
    feature_id: int
    author_id: int
    title: str
    description: str
    type: RequirementType
    status: RequirementStatus
    priority: RequirementPriority
    complexity: RequirementComplexity
    assignee_id: Optional[int] = None
    expected_completion_date: Optional[datetime] = None
