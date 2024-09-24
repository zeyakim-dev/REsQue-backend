from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.domains.requirement.value_objects import (
    RequirementComplexity,
    RequirementPriority,
    RequirementStatus,
    RequirementType,
)

Base = declarative_base()


class SQLRequirement(Base):
    __tablename__ = "requirements"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)

    feature_id = Column(Integer, ForeignKey("features.id"), nullable=False, index=True)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    title = Column(String(255), nullable=False, index=True)
    description = Column(String(1000), nullable=False)

    type = Column(Enum(RequirementType), nullable=False)
    status = Column(
        Enum(RequirementStatus), nullable=False, default=RequirementStatus.TODO
    )
    priority = Column(Enum(RequirementPriority), nullable=False)
    complexity = Column(Enum(RequirementComplexity), nullable=False)

    assignee_id = Column(Integer, ForeignKey("users.id"), nullable=True, index=True)
    expected_completion_date = Column(DateTime, nullable=True)

    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

    is_deleted = Column(Boolean)
    deleted_at = Column(DateTime(timezone=True), nullable=True)

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
