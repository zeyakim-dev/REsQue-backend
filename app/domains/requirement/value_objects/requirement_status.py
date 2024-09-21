from enum import Enum, auto


class RequirementStatus(Enum):
    TODO = auto()
    IN_PROGRESS = auto()
    REVIEW = auto()
    DONE = auto()
