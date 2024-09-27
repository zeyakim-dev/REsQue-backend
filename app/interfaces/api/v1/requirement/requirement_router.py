from fastapi import APIRouter, Query
from typing import List, Optional
from uuid import UUID

from app.application.dto.requirement_dto import (
    CreateRequirementRequestDTO,
    UpdateRequirementRequestDTO,
    RequirementResponseDTO,
    PaginatedRequirementResponseDTO,
)
from app.application.use_cases.requirement.requirement_use_cases import (
    CreateRequirementUseCase,
    UpdateRequirementUseCase,
    DeleteRequirementUseCase,
    GetRequirementUseCase,
    ListRequirementUseCase,
)
from app.infrastructure.database.unit_of_works.sql_unit_of_work import (
    SQLAlchemyUnitOfWork,
)


class RequirementV1Router(APIRouter):
    def __init__(self):
        super().__init__()
        self.prefix = "/api/v1/requirements"
        self.tags = ["requirements"]

        self.add_api_routes()

    def add_api_routes(self):
        self.add_api_route(
            "/",
            self.create_requirement,
            methods=["POST"],
            response_model=RequirementResponseDTO,
        )
        self.add_api_route(
            "/{requirement_id}",
            self.update_requirement,
            methods=["PUT"],
            response_model=RequirementResponseDTO,
        )
        self.add_api_route(
            "/{requirement_id}",
            self.delete_requirement,
            methods=["DELETE"],
            status_code=204,
        )
        self.add_api_route(
            "/{requirement_id}",
            self.get_requirement,
            methods=["GET"],
            response_model=RequirementResponseDTO,
        )
        self.add_api_route(
            "/",
            self.list_requirements,
            methods=["GET"],
            response_model=PaginatedRequirementResponseDTO,
        )

    async def create_requirement(
        self,
        requirement: CreateRequirementRequestDTO,
    ):
        uow = SQLAlchemyUnitOfWork()
        use_case = CreateRequirementUseCase(uow)
        return await use_case.execute(requirement)

    async def update_requirement(
        self,
        requirement_id: UUID,
        requirement: UpdateRequirementRequestDTO,
    ):
        uow = SQLAlchemyUnitOfWork()
        use_case = UpdateRequirementUseCase(uow)
        requirement.id = requirement_id
        return await use_case.execute(requirement)

    async def delete_requirement(
        self,
        requirement_id: UUID,
    ):
        uow = SQLAlchemyUnitOfWork()
        use_case = DeleteRequirementUseCase(uow)
        await use_case.execute(requirement_id)

    async def get_requirement(
        self,
        requirement_id: UUID,
    ):
        uow = SQLAlchemyUnitOfWork()
        use_case = GetRequirementUseCase(uow)
        return await use_case.execute(requirement_id)

    async def list_requirements(
        self,
        page: int = Query(1, ge=1),
        per_page: int = Query(20, ge=1, le=100),
        filters: Optional[str] = Query(None),
        order_by: Optional[List[str]] = Query(None),
    ):
        uow = SQLAlchemyUnitOfWork()
        use_case = ListRequirementUseCase(uow)
        return await use_case.execute(
            filters=filters, order_by=order_by, page=page, per_page=per_page
        )


requirement_router = RequirementV1Router()
