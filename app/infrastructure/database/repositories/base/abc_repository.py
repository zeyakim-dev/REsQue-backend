from abc import ABC, abstractmethod
from typing import Dict, Optional, Tuple, NamedTuple, Any

from uuid import UUID
from app.domains.requirement.repositories.requirement_repository import PageInfo
from app.shared.domains.entities.paginated_entities import PaginatedEntities
from app.shared.domains.entities.base_entity import BaseEntity
from app.infrastructure.database.models.base_model import BaseModel
from app.shared.domains.entities.query_params import QueryParams


class ABCRepository(ABC):
    pass


class PaginatedModels(NamedTuple):
    models: Tuple[BaseModel, ...]
    total: int
    total_pages: int
    page: int
    per_page: int


class CRUDRepository(ABCRepository):
    @abstractmethod
    def _to_entity(self, model: BaseModel) -> BaseEntity:
        pass

    @abstractmethod
    def _to_model(self, entity: BaseEntity) -> BaseModel:
        pass

    async def create(self, entity: BaseEntity) -> BaseEntity:
        try:
            model = self._to_model(entity)
            created_model = await self._create(model)
            created_entity = self._to_entity(created_model)
        except:
            raise

        return created_entity

    @abstractmethod
    async def _create(self, model: BaseModel) -> BaseModel:
        pass

    async def get(self, id: UUID) -> Optional[BaseEntity]:
        try:
            model = await self._get(id)
            return self._to_entity(model) if model else None
        except:
            raise

    @abstractmethod
    async def _get(self, id: UUID) -> Optional[BaseModel]:
        pass

    async def update(self, id: UUID, update_data: Dict[str, Any]) -> BaseEntity:
        try:
            existing_model = await self._get(id)
            if not existing_model:
                raise

            updated_model = await self._update(existing_model, update_data)
            return self._to_entity(updated_model)
        except:
            raise

    @abstractmethod
    async def _update(
        self, existing_model: BaseModel, update_data: Dict[str, Any]
    ) -> BaseModel:
        pass

    async def delete(self, id: UUID) -> None:
        try:
            model = await self._get(id)
            await self._delete(model)
        except:
            raise

    @abstractmethod
    async def _delete(self, model: BaseModel) -> None:
        pass

    async def query(
        self, page_info: PageInfo, query_params: QueryParams
    ) -> PaginatedEntities:
        try:
            filters = query_params.filters
            orderings = query_params.orderings

            paginated_results = await self._query(page_info, filters, orderings)

            entities = tuple(
                self._to_entity(model) for model in paginated_results["models"]
            )

            return PaginatedEntities(
                entities=entities,
                total_count=paginated_results.total_count,
                page=paginated_results.page,
                per_page=paginated_results.per_page,
            )
        except:
            raise

    @abstractmethod
    async def _query(
        self, page_info, filters: Dict[str, Any], orderings: Tuple[str, ...]
    ) -> PaginatedModels:
        pass
