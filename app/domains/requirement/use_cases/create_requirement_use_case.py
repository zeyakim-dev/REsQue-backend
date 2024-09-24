from app.domains.requirement.dto import (
    CreateRequirementRequestDTO,
    CreateRequirementResponseDTO,
)
from app.domains.requirement.entities import Requirement as RequirementEntity
from app.domains.requirement.repositories import RequirementRepository


class CreateRequirementUseCase:
    def __init__(self, requirement_repository: RequirementRepository):
        self.requirement_repository = requirement_repository

    def execute(self, dto: CreateRequirementRequestDTO) -> RequirementEntity:
        requirement = RequirementEntity()
        created_requirment_entity = self.requirement_repository.create(requirement)

        return CreateRequirementResponseDTO(created_requirment_entity)
