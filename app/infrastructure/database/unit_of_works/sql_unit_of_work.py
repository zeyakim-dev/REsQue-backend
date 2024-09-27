from sqlalchemy.ext.asyncio import AsyncSession

from app.domains.requirement.repositories.requirement_repository import RequirementRepository
from app.domains.requirement.infrastructure.database.repositories.sql_requirement_repository import SQLAlchemyRequirementRepository
from app.infrastructure.database.unit_of_works.unit_of_work import UnitOfWork


class SQLAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session: AsyncSession = self.session_factory()
        return self

    async def _commit(self):
        await self.session.commit()

    async def _rollback(self):
        await self.session.rollback()

    def get_requirement_repository(self) -> RequirementRepository:
        return SQLAlchemyRequirementRepository(self.session)
