from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from app.shared.domains.entities.base_entity import BaseEntity
from app.shared.domains.mixins.soft_deletion_mixin import SoftDeletionMixin
from app.shared.domains.mixins.timestamp_mixin import TimestampMixin


@dataclass(kw_only=True, frozen=True)
class Document(BaseEntity, TimestampMixin, SoftDeletionMixin):
    project_id: int
    title: str
    description: str
    base_domain_id: Optional[int] = None
    content: str = ""
    version: int = 1
