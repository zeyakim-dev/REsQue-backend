from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID, uuid4

@dataclass(frozen=True)
class BaseEntity:
    id: UUID = field(default_factory=uuid4)