from dataclasses import dataclass, field


@dataclass
class BaseEntity:
    id: int = field(default=None)
