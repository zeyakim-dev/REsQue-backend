from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime
from app.shared.domain.base_entity import BaseEntity
from app.shared.domain.mixin.timestamp_mixin import TimestampMixin
from app.shared.domain.mixin.soft_deletion_mixin import SoftDeletionMixin
from app.domains.requirement.value_objects.requirement_complexity import RequirementComplexity
from app.domains.requirement.value_objects.requirement_priority import RequirementPriority
from app.domains.requirement.value_objects.requirement_status import RequirementStatus
from app.domains.requirement.value_objects.requirement_type import RequirementType

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