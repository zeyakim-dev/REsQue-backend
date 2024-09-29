from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from app.shared.domains.entities.base_entity import BaseEntity
from app.shared.domains.mixins.soft_deletion_mixin import SoftDeletionMixin
from app.shared.domains.mixins.timestamp_mixin import TimestampMixin


@dataclass(kw_only=True, frozen=True)
class Domain(BaseEntity, TimestampMixin, SoftDeletionMixin):
    document_id: int
    name: str
    description: str
