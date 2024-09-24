from abc import ABC, abstractmethod
from typing import List, Tuple, Optional
from uuid import UUID
from dataclasses import dataclass

from app.domains.requirement.entities.requirement import Requirement as RequirementEntity
from app.domains.requirement.adapters.mappers.requirement_mapper import RequirementMapper
from app.domains.requirement.infrastructure.database.models.base.requirement import RequirementModel

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
    async def list_paginated(self, page: int = 1, per_page: int = 20) -> PaginatedResult:
        """페이지네이션된 요구사항 목록을 조회합니다."""
        try:
            models, total = await self._list_paginated(page, per_page)
            items = [RequirementMapper.to_entity(model) for model in models]
            total_pages = (total - 1) // per_page + 1
            page_info = PageInfo(page=page, per_page=per_page, total=total, total_pages=total_pages)
            return PaginatedResult(items=items, page_info=page_info)
        except Exception as e:
            # 적절한 예외 처리 로직 추가
            raise

    @abstractmethod
    async def _list_paginated(self, page: int = 1, per_page: int = 20) -> Tuple[List[RequirementModel], int]:
        """페이지네이션된 요구사항 모델과 전체 개수를 조회합니다."""
        pass

    async def create(self, requirement: RequirementEntity) -> RequirementEntity:
        try:
            requirement_model = RequirementMapper.to_model(requirement)
            await self._save(requirement_model)
            return RequirementMapper.to_entity(requirement_model)
        except Exception as e:
            # 적절한 예외 처리 로직 추가
            raise

    async def get_by_id(self, id: UUID) -> Optional[RequirementEntity]:
        try:
            requirement_model = await self._get(id)
            return RequirementMapper.to_entity(requirement_model) if requirement_model else None
        except Exception as e:
            # 적절한 예외 처리 로직 추가
            raise

    async def update(self, id: UUID, requirement: RequirementEntity) -> RequirementEntity:
        try:
            requirement_model = await self._get(id)
            if requirement_model is None:
                raise ValueError(f"Requirement with id {id} not found")
            requirement_model.update(requirement)
            await self._save(requirement_model)
            return RequirementMapper.to_entity(requirement_model)
        except Exception as e:
            # 적절한 예외 처리 로직 추가
            raise

    async def delete(self, id: UUID) -> bool:
        try:
            requirement_model = await self._get(id)
            if requirement_model is None:
                return False
            return await self._delete(requirement_model)
        except Exception as e:
            # 적절한 예외 처리 로직 추가
            raise

    @abstractmethod
    async def _save(self, requirement_model: RequirementModel) -> None:
        pass

    @abstractmethod
    async def _get(self, id: UUID) -> Optional[RequirementModel]:
        pass
    
    @abstractmethod
    async def _delete(self, requirement_model: RequirementModel) -> bool:
        pass

    async def _filter(self, *args):
        # 필터링 로직 구현
        pass