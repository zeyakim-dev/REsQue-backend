from dataclasses import asdict
from typing import Any, Type

from app.domains.requirement.dto.create_requirement_dto import (
    CreateRequirementRequestDTO,
    CreateRequirementResponseDTO,
)
from app.domains.requirement.entities.requirement import (
    Requirement as RequirementEntity,
)
from app.domains.requirement.infrastructure.database.models.sql.sql_requirment import (
    SQLRequirement as RequirementModel,
)


class RequirementMapper:
    @staticmethod
    def model_to_dict(model: RequirementModel):
        return {c.name: getattr(model, c.name) for c in model.__table__.columns}

    @staticmethod
    def model_to_entity(model: RequirementModel) -> RequirementEntity:
        model_dict = RequirementMapper.model_to_dict(model)
        return RequirementEntity(**model_dict)

    @staticmethod
    def entity_to_model(entity: RequirementEntity) -> RequirementModel:
        entity_dict = asdict(entity)
        return RequirementModel(**entity_dict)

    @staticmethod
    def request_to_entity(request: CreateRequirementRequestDTO) -> RequirementEntity:
        request_dict = asdict(request)
        return RequirementEntity(**request_dict)

    @staticmethod
    def entity_to_response(entity: RequirementEntity) -> CreateRequirementResponseDTO:
        entity_dict = asdict(entity)
        return CreateRequirementResponseDTO(**entity_dict)
