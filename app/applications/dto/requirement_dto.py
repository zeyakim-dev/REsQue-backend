from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, Optional, Tuple
from uuid import UUID

from app.applications.dto.abc_dto import (
    PageQueryInfoDTO,
    RequestDTO,
    ResponseDTO,
    SoftDeletionDTO,
    TimestampDTO,
    TrackedDTO,
)
from app.domains.requirement.value_objects import (
    RequirementComplexity,
    RequirementPriority,
    RequirementStatus,
    RequirementType,
)


class ABCRequirementDTO(TrackedDTO):
    title: str
    description: str
    feature_id: int
    author_id: int
    type: RequirementType
    priority: RequirementPriority
    complexity: RequirementComplexity
    status: RequirementStatus = RequirementStatus.TODO
    assignee_id: Optional[int] = None
    expected_completion_date: Optional[datetime] = None


class CreateRequirementRequestDTO(ABCRequirementDTO, RequestDTO):
    pass


class ABCTrackedRequirementDTO(
    ABCRequirementDTO, TimestampDTO, TrackedDTO, SoftDeletionDTO
):
    pass


class UpdateRequirementRequestDTO(ABCTrackedRequirementDTO, RequestDTO):
    pass


class PageQueryRequirementRequestDTO(PageQueryInfoDTO, RequestDTO):
    pass


class RequirementResponseDTO(ABCTrackedRequirementDTO, ResponseDTO):
    pass
