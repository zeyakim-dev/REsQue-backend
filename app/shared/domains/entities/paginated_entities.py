from dataclasses import dataclass
from typing import Tuple

from app.shared.domains.entities.base_entity import BaseEntity


@dataclass(kw_only=True, frozen=True)
class PaginatedEntities:
    entities: Tuple[BaseEntity, ...]
    total: int
    total_pages: int
    page: int
    per_page: int
