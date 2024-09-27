from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID


@dataclass(kw_only=True, frozen=True)
class ABCDTO(ABC):
    pass


@dataclass(kw_only=True, frozen=True)
class ABCTrackedDTO(ABC):
    id: UUID


@dataclass(kw_only=True, frozen=True)
class ABCTimestampDTO(ABC):
    created_at: datetime
    updated_at: datetime


@dataclass(kw_only=True, frozen=True)
class ABCSoftDeletionDTO(ABC):
    is_deleted: bool
    deleted_at: Optional[datetime] = None
