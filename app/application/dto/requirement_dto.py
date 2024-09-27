from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List
from uuid import UUID

from app.application.dto.abc_dto import (
    ABCDTO,
    ABCSoftDeletionDTO,
    ABCTimestampDTO,
    ABCTrackedDTO,
)
from app.domains.requirement.value_objects import (
    RequirementComplexity,
    RequirementPriority,
    RequirementStatus,
    RequirementType,
)


@dataclass(kw_only=True, frozen=True)
class ABCRequirementDTO(ABCDTO):
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


@dataclass(kw_only=True, frozen=True)
class CreateRequirementRequestDTO(ABCRequirementDTO):
    pass


@dataclass(kw_only=True, frozen=True)
class ABCTrackedRequirementDTO(
    ABCRequirementDTO, ABCTimestampDTO, ABCTrackedDTO, ABCSoftDeletionDTO
):
    pass


@dataclass(kw_only=True, frozen=True)
class UpdateRequirementRequestDTO(ABCTrackedRequirementDTO):
    pass


@dataclass(kw_only=True, frozen=True)
class RequirementResponseDTO(ABCTrackedRequirementDTO):
    pass


@dataclass(kw_only=True, frozen=True)
class PageInfoDTO:
    page: int
    per_page: int
    total: int
    total_pages: int


@dataclass(kw_only=True, frozen=True)
class PaginatedRequirementResponseDTO:
    items: List[RequirementResponseDTO]
    page_info: PageInfoDTO
