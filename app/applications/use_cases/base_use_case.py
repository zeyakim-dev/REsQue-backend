from abc import ABC, abstractmethod

from app.applications.dto.abc_dto import ABCDTO
from app.infrastructure.database.unit_of_works.unit_of_work import UnitOfWork


class ABCUseCase(ABC):
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    @abstractmethod
    async def _execute_logic(self, dto: ABCDTO):
        pass

    async def execute(self, dto: ABCDTO):
        async with self.uow:
            return await self._execute_logic(dto)
