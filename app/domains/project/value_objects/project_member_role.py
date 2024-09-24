from enum import Enum, auto


class ProjectMemberRole(Enum):
    OWNER = auto()
    ADMIN = auto()
    MEMBER = auto()
    VIEWER = auto()
