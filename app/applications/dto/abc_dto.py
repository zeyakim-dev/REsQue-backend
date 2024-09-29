from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, Optional, Tuple
from uuid import UUID


@dataclass(kw_only=True, frozen=True)
class ABCDTO(ABC):
    pass


class TrackedDTO(ABCDTO):
    id: UUID


class TimestampDTO(ABCDTO):
    created_at: datetime
    updated_at: datetime


class SoftDeletionDTO(ABCDTO):
    is_deleted: bool
    deleted_at: Optional[datetime] = None


class RequestDTO(ABCDTO):
    pass


class ResponseDTO(ABCDTO):
    pass


class PageQueryInfoDTO(RequestDTO):
    page: int
    per_page: int
    filters: Dict[str, Any]
    orderings: Tuple[str, ...]


class PaginatedResponseDTO(ResponseDTO):
    page: int
    per_page: int
    total: int
    total_pages: int
    dtos: Tuple[ResponseDTO, ...]
