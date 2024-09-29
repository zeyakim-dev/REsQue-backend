from dataclasses import dataclass, replace
from datetime import datetime
from typing import Optional

from app.domains.requirement.value_objects import (
    RequirementComplexity,
    RequirementPriority,
    RequirementStatus,
    RequirementType,
)
from app.shared.domains.entities.base_entity import BaseEntity
from app.shared.domains.mixins.soft_deletion_mixin import SoftDeletionMixin
from app.shared.domains.mixins.timestamp_mixin import TimestampMixin


@dataclass(frozen=True, kw_only=True)
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

    def update(self, updating_entity: "Requirement") -> "Requirement":
        updatable_attrs = [
            "feature_id",
            "title",
            "description",
            "type",
            "status",
            "priority",
            "complexity",
            "assignee_id",
            "expected_completion_date",
        ]

        update_dict = {
            attr: getattr(updating_entity, attr)
            for attr in updatable_attrs
            if getattr(updating_entity, attr) != getattr(self, attr)
        }

        if update_dict:
            update_dict["updated_at"] = datetime.now()
            return replace(self, **update_dict)

        return self
