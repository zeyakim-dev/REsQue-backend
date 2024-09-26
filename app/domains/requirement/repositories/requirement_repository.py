from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple
from uuid import UUID

from app.application.mappers.requirement_mapper import RequirementMapper
from app.domains.requirement.entities.requirement import (
    Requirement as RequirementEntity,
)
from app.domains.requirement.infrastructure.database.models.base.requirement import ABCRequirementModel


@dataclass
class PageInfo:
    page: int
    per_page: int
    total: int
    total_pages: int


@dataclass
class PaginatedResult:
    items: List[RequirementEntity]
    page_info: PageInfo


class RequirementRepository(ABC):
    @abstractmethod
    async def _find_model_by_id(self, id: UUID) -> Optional[ABCRequirementModel]:
        pass

    async def create(self, requirement: RequirementEntity) -> RequirementEntity:
        try:
            model = RequirementMapper.entity_to_model(requirement)

            created_model = await self._save(model)
            return RequirementMapper.model_to_entity(created_model)
        except Exception as e:
            # 적절한 예외 처리 로직 추가
            raise

    async def get_by_id(self, id: UUID) -> Optional[RequirementEntity]:
        try:
            model = await self._find_model_by_id(id)

            return RequirementMapper.model_to_entity(model) if model else None
        except Exception as e:
            # 적절한 예외 처리 로직 추가
            raise

    async def update(self, entity: RequirementEntity) -> RequirementEntity:
        try:
            id = entity.id
            model = await self._find_model_by_id(id)
            if model is None:
                raise ValueError(f"Requirement with id {id} not found")

            updated_model = await self._update(entity, model)
            return RequirementMapper.model_to_entity(updated_model)
        except Exception as e:
            # 적절한 예외 처리 로직 추가
            raise

    @abstractmethod
    async def _update(
        self, updated_entity: RequirementEntity, updating_model: ABCRequirementModel
    ) -> ABCRequirementModel:
        pass

    async def delete(self, id: UUID) -> bool:
        try:
            model = await self._find_model_by_id(id)
            if model is None:
                return False
            return await self._delete(model)
        except Exception as e:
            # 적절한 예외 처리 로직 추가
            raise

    @abstractmethod
    async def _save(self, requirement_model: ABCRequirementModel) -> ABCRequirementModel:
        pass

    @abstractmethod
    async def _delete(self, requirement_model: ABCRequirementModel) -> bool:
        pass

    @abstractmethod
    async def _execute_filtered_query(
        self,
        filters: Optional[Dict[str, Any]],
        order_by: Optional[List[str]],
        page: int,
        per_page: int,
    ) -> Tuple[List[ABCRequirementModel], int]:
        """필터링된 쿼리를 실행하고 결과를 반환하는 메서드. 하위 클래스에서 구현해야 함."""
        pass

    async def list_filtered_and_ordered(
        self,
        filters: Optional[Dict[str, Any]] = None,
        order_by: Optional[List[str]] = None,
        page: int = 1,
        per_page: int = 20,
    ) -> PaginatedResult:
        try:
            models, total = await self._execute_filtered_query(
                filters, order_by, page, per_page
            )
            items = [RequirementMapper.model_to_entity(model) for model in models]
            total_pages = (total - 1) // per_page + 1
            page_info = PageInfo(
                page=page, per_page=per_page, total=total, total_pages=total_pages
            )
            return PaginatedResult(items=items, page_info=page_info)
        except Exception as e:
            # 적절한 예외 처리 로직 추가
            raise
