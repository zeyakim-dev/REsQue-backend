from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domains.requirement.entities import Requirement as RequirementEntity
from app.domains.requirement.infrastructure.database.models.sql.sql_requirment import (
    SQLRequirement as RequirementModel,
)
from app.domains.requirement.repositories import RequirementRepository


class SQLAlchemyRequirementRepository(RequirementRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, requirement: RequirementEntity) -> RequirementEntity:
        model = RequirementModel(
            title=requirement.title,
            description=requirement.description,
            status=requirement.status,
            created_at=requirement.created_at,
            updated_at=requirement.updated_at,
        )
        self.session.add(model)
        await self.session.flush()
        requirement.id = model.id
        return requirement

    async def get_by_id(self, id: int) -> Optional[RequirementEntity]:
        result = await self.session.execute(select(RequirementModel).filter_by(id=id))
        model = result.scalar_one_or_none()
        return self._model_to_entity(model) if model else None

    async def list_all(self) -> List[RequirementEntity]:
        result = await self.session.execute(select(RequirementModel))
        return [self._model_to_entity(model) for model in result.scalars().all()]

    async def update(self, requirement: RequirementEntity) -> RequirementEntity:
        model = await self.session.get(RequirementModel, requirement.id)
        if model:
            model.title = requirement.title
            model.description = requirement.description
            model.status = requirement.status
            model.updated_at = requirement.updated_at
            await self.session.flush()
        return requirement

    async def delete(self, requirement_id: int) -> bool:
        model = await self.session.get(RequirementModel, requirement_id)
        if model:
            await self.session.delete(model)
            return True
        return False

    def _model_to_entity(self, model: RequirementModel) -> RequirementEntity:
        return RequirementEntity(
            id=model.id,
            title=model.title,
            description=model.description,
            status=model.status,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )
