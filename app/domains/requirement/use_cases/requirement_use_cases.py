from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from uuid import UUID

from app.application.dto.requirement_dto import (
    CreateRequirementRequestDTO,
    PaginatedRequirementResponseDTO,
    RequirementResponseDTO,
    UpdateRequirementRequestDTO,
)
from app.application.mappers.requirement_mapper import RequirementMapper
from app.domains.requirement.entities import Requirement as RequirementEntity
from app.domains.requirement.repositories.requirement_repository import PaginatedResult
from app.infrastructure.database.unit_of_works.unit_of_work import UnitOfWork


class ABCRequirementUseCase(ABC):
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    @abstractmethod
    async def _execute_logic(self, dto):
        pass

    async def execute(self, dto):
        async with self.uow:
            return await self._execute_logic(dto)


class CreateRequirementUseCase(ABCRequirementUseCase):
    async def _execute_logic(
        self, dto: CreateRequirementRequestDTO
    ) -> RequirementResponseDTO:
        requirement: RequirementEntity = RequirementMapper.request_to_entity(dto)
        repo = self.uow.get_requirement_repository()
        created_requirement_entity = await repo.create(requirement)
        return RequirementMapper.entity_to_response(created_requirement_entity)


class UpdateRequirementUseCase(ABCRequirementUseCase):
    async def _execute_logic(
        self, dto: UpdateRequirementRequestDTO
    ) -> RequirementResponseDTO:
        requirement: RequirementEntity = RequirementMapper.request_to_entity(dto)
        repo = self.uow.get_requirement_repository()
        updated_requirement_entity = await repo.update(requirement)
        return RequirementMapper.entity_to_response(updated_requirement_entity)


class DeleteRequirementUseCase(ABCRequirementUseCase):
    async def _execute_logic(self, id: UUID) -> None:
        repo = self.uow.get_requirement_repository()
        await repo.delete(id)


class GetRequirementUseCase(ABCRequirementUseCase):
    async def _execute_logic(self, id: UUID) -> RequirementResponseDTO:
        repo = self.uow.get_requirement_repository()
        requirement_entity = await repo.get_by_id(id)
        if not requirement_entity:
            raise
        
        return RequirementMapper.entity_to_response(requirement_entity)


class ListRequirementUseCase(ABCRequirementUseCase):
    async def _execute_logic(
        self,
        filters: Optional[Dict[str, Any]] = None,
        order_by: Optional[List[str]] = None,
        page: int = 1,
        per_page: int = 20,
    ) -> PaginatedRequirementResponseDTO:
        repo = self.uow.get_requirement_repository()
        paginated_result: PaginatedResult = await repo.list_filtered_and_ordered(
            filters=filters, order_by=order_by, page=page, per_page=per_page
        )

        requirement_dtos = [
            RequirementMapper.entity_to_response(entity)
            for entity in paginated_result.items
        ]

        return PaginatedRequirementResponseDTO(
            items=requirement_dtos, page_info=paginated_result.page_info
        )
