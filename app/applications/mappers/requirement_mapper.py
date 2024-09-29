from dataclasses import asdict
from typing import Any, Type

from app.applications.dto.requirement_dto import (
    ABCRequirementDTO,
    RequirementResponseDTO,
)
from app.domains.requirement.entities.requirement import (
    Requirement as RequirementEntity,
)
from app.domains.requirement.infrastructure.database.models.base.requirement import (
    RequirementModel,
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
    def request_to_entity(request: ABCRequirementDTO) -> RequirementEntity:
        request_dict = asdict(request)
        return RequirementEntity(**request_dict)

    @staticmethod
    def entity_to_response(entity: RequirementEntity) -> RequirementResponseDTO:
        entity_dict = asdict(entity)
        return RequirementResponseDTO(**entity_dict)
