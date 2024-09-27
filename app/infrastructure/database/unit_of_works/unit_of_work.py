from abc import ABC, abstractmethod
from typing import Type

from app.domains.requirement.repositories import RequirementRepository


class UnitOfWork(ABC):
    @abstractmethod
    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if exc_type is None:
            await self._commit()
        else:
            await self._rollback()

    @abstractmethod
    async def _commit(self):
        pass

    @abstractmethod
    async def _rollback(self):
        pass

    @abstractmethod
    def get_requirement_repository(self) -> RequirementRepository:
        pass
