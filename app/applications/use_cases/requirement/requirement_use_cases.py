from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from uuid import UUID

from app.applications.dto.requirement_dto import (
    CreateRequirementRequestDTO,
    PaginatedRequirementResponseDTO,
    RequirementResponseDTO,
    UpdateRequirementRequestDTO,
)
from app.applications.mappers.requirement_mapper import RequirementMapper
from app.applications.use_cases.base_use_case import ABCUseCase
from app.domains.requirement.entities import Requirement as RequirementEntity
from app.domains.requirement.repositories.requirement_repository import PaginatedResult


class CreateRequirementUseCase(ABCUseCase):
    async def _execute_logic(
        self, dto: CreateRequirementRequestDTO
    ) -> RequirementResponseDTO:
        requirement: RequirementEntity = RequirementMapper.request_to_entity(dto)
        repo = self.uow.get_requirement_repository()
        created_requirement_entity = await repo.create(requirement)
        return RequirementMapper.entity_to_response(created_requirement_entity)


class UpdateRequirementUseCase(ABCUseCase):
    async def _execute_logic(
        self, dto: UpdateRequirementRequestDTO
    ) -> RequirementResponseDTO:
        requirement: RequirementEntity = RequirementMapper.request_to_entity(dto)
        repo = self.uow.get_requirement_repository()
        updated_requirement_entity = await repo.update(requirement)
        return RequirementMapper.entity_to_response(updated_requirement_entity)


class DeleteRequirementUseCase(ABCUseCase):
    async def _execute_logic(self, id: UUID) -> None:
        repo = self.uow.get_requirement_repository()
        await repo.delete(id)


class GetRequirementUseCase(ABCUseCase):
    async def _execute_logic(self, id: UUID) -> RequirementResponseDTO:
        repo = self.uow.get_requirement_repository()
        requirement_entity = await repo.get_by_id(id)
        if not requirement_entity:
            raise

        return RequirementMapper.entity_to_response(requirement_entity)


class ListRequirementUseCase(ABCUseCase):
    async def _execute_logic(
        self,
        filters: Optional[Dict[str, Any]] = None,
        order_by: Optional[List[str]] = None,
        page: int = 1,
        per_page: int = 20,
    ) -> PaginatedRequirementResponseDTO:
        repo = self.uow.get_requirement_repository()
        paginated_result: Optional[PaginatedResult] = (
            await repo.list_filtered_and_ordered(
                filters=filters, order_by=order_by, page=page, per_page=per_page
            )
        )

        if not paginated_result:
            return None

        requirement_dtos = [
            RequirementMapper.entity_to_response(entity)
            for entity in paginated_result.items
        ]

        return PaginatedRequirementResponseDTO(
            items=requirement_dtos, page_info=paginated_result.page_info
        )
