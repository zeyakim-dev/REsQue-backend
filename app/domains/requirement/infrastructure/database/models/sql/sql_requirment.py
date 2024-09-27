import uuid
from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.domains.requirement.infrastructure.database.models.base.requirement import (
    RequirementModel,
)
from app.domains.requirement.value_objects import (
    RequirementComplexity,
    RequirementPriority,
    RequirementStatus,
    RequirementType,
)
from app.infrastructure.database.models.sql_model import SQLAlchemyModel


class SQLRequirementModel(SQLAlchemyModel, RequirementModel):
    __tablename__ = "requirements"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, index=True
    )
    feature_id: Mapped[int] = mapped_column(
        ForeignKey("features.id"), nullable=False, index=True
    )
    author_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=False, index=True
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    description: Mapped[str] = mapped_column(String(1000), nullable=False)
    type: Mapped[RequirementType] = mapped_column(Enum(RequirementType), nullable=False)
    status: Mapped[RequirementStatus] = mapped_column(
        Enum(RequirementStatus), nullable=False
    )
    priority: Mapped[RequirementPriority] = mapped_column(
        Enum(RequirementPriority), nullable=False
    )
    complexity: Mapped[RequirementComplexity] = mapped_column(
        Enum(RequirementComplexity), nullable=False
    )
    assignee_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id"), nullable=True, index=True
    )
    expected_completion_date: Mapped[datetime | None] = mapped_column(
        DateTime, nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), onupdate=func.now(), nullable=True
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    # ... (나머지 코드는 동일)

    # Relationships (주석 처리된 상태로 두어 현재는 사용하지 않지만 나중에 필요할 때 쉽게 추가할 수 있게 합니다)
    # feature = relationship("Feature", back_populates="requirements")
    # author = relationship("User", foreign_keys=[author_id], back_populates="authored_requirements")
    # assignee = relationship("User", foreign_keys=[assignee_id], back_populates="assigned_requirements")

    __table_args__ = (
        # 복합 인덱스 예시 (성능 최적화에 도움이 될 수 있는 경우 사용)
        # Index('idx_feature_status', feature_id, status),
    )

    def __repr__(self):
        return (
            f"<Requirement(id={self.id}, title='{self.title}', status={self.status})>"
        )
