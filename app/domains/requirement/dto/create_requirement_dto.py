from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.domains.requirement.value_objects import RequirementComplexity, RequirementPriority, RequirementStatus, RequirementType

class CreateRequirementRequestDTO(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: str = Field(..., min_length=1)
    feature_id: int = Field(..., gt=0)
    author_id: int = Field(..., gt=0)
    
    type: RequirementType
    status: RequirementStatus = Field(default=RequirementStatus.TODO)
    priority: RequirementPriority
    complexity: RequirementComplexity
    
    assignee_id: Optional[int] = Field(None, gt=0)
    expected_completion_date: Optional[datetime] = None

class CreateRequirementResponseDTO(BaseModel):
    id: int = Field(..., gt=0)

    title: str = Field(..., min_length=1, max_length=200)
    description: str = Field(..., min_length=1)
    feature_id: int = Field(..., gt=0)
    author_id: int = Field(..., gt=0)
    
    type: RequirementType
    status: RequirementStatus
    priority: RequirementPriority
    complexity: RequirementComplexity
    
    assignee_id: Optional[int] = Field(None, gt=0)
    expected_completion_date: Optional[datetime] = None
    
    created_at: datetime
    updated_at: datetime

    is_deleted: bool
    deleted_at: Optional[datetime] = None