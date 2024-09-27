from abc import ABC
from typing import Any


class BaseModel(ABC):
    id: Any


class DomainConceptModel(BaseModel): ...


class PersistenceModel(BaseModel): ...
