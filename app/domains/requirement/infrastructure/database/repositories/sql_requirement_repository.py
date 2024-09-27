from dataclasses import asdict
from typing import Any, Dict, List, Optional, Sequence, Tuple
from uuid import UUID

from sqlalchemy import asc, desc, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.selectable import Select

from app.application.mappers.requirement_mapper import RequirementMapper
from app.domains.requirement.entities.requirement import (
    Requirement as RequirementEntity,
)
from app.domains.requirement.infrastructure.database.models.base.requirement import (
    RequirementModel,
)
from app.domains.requirement.repositories.requirement_repository import (
    RequirementRepository,
)


class SQLAlchemyRequirementRepository(RequirementRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def _find_model_by_id(self, id: UUID) -> Optional[RequirementModel]:
        statement = select(RequirementModel).where(RequirementModel.id == id)
        result = await self.session.execute(statement)
        return result.scalar_one_or_none()

    async def _save(self, requirement_model: RequirementModel) -> RequirementModel:
        self.session.add(requirement_model)
        await self.session.flush()
        await self.session.refresh(requirement_model)
        return requirement_model

    async def get_by_id(self, id: UUID) -> Optional[RequirementEntity]:
        model = await self._find_model_by_id(id)
        return RequirementMapper.model_to_entity(model) if model else None

    async def _update(
        self, updated_entity: RequirementEntity, updating_model: RequirementModel
    ) -> RequirementModel:
        for key, value in asdict(updated_entity).items():

            if key != "id" and hasattr(updating_model, key):
                setattr(updating_model, key, value)

        await self.session.flush()
        await self.session.refresh(updating_model)
        return updating_model

    async def _delete(self, model: RequirementModel) -> bool:
        await self.session.delete(model)
        await self.session.flush()
        return True

    def _apply_filters(
        self, query: Select, filters: Optional[Dict[str, Any]]
    ) -> Select:
        if filters:
            for key, value in filters.items():
                if hasattr(RequirementModel, key):
                    query = query.where(getattr(RequirementModel, key) == value)
        return query

    def _apply_ordering(self, query: Select, order_by: Optional[List[str]]) -> Select:
        if order_by:
            for field in order_by:
                direction = desc if field.startswith("-") else asc
                field = field.lstrip("-")
                if hasattr(RequirementModel, field):
                    query = query.order_by(direction(getattr(RequirementModel, field)))
        return query

    def _apply_pagination(self, query: Select, page: int, per_page: int) -> Select:
        return query.offset((page - 1) * per_page).limit(per_page)

    async def _execute_filtered_query(
        self,
        filters: Optional[Dict[str, Any]],
        order_by: Optional[List[str]],
        page: int,
        per_page: int,
    ) -> Tuple[Sequence[RequirementModel], int | None]:
        query = select(RequirementModel)

        query = self._apply_filters(query, filters)
        query = self._apply_ordering(query, order_by)

        count_query = select(func.count()).select_from(query.subquery())
        total = await self.session.scalar(count_query)

        query = self._apply_pagination(query, page, per_page)

        result = await self.session.execute(query)
        items = result.scalars().all()

        return items, total
