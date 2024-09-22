from abc import ABC, abstractmethod
from typing import List, Optional

from app.domains.requirement.entities.requirement import Requirement


class RequirementRepository(ABC):
    @abstractmethod
    async def create(self, requirement: Requirement) -> Requirement:
        """새로운 요구사항을 생성합니다."""
        pass

    @abstractmethod
    async def get_by_id(self, requirement_id: int) -> Optional[Requirement]:
        """ID로 요구사항을 조회합니다."""
        pass

    @abstractmethod
    async def get_all(self) -> List[Requirement]:
        """모든 요구사항을 조회합니다."""
        pass

    @abstractmethod
    async def update(self, requirement: Requirement) -> Requirement:
        """요구사항을 업데이트합니다."""
        pass

    @abstractmethod
    async def delete(self, requirement_id: int) -> bool:
        """요구사항을 삭제합니다."""
        pass

    @abstractmethod
    async def get_by_feature_id(self, feature_id: int) -> List[Requirement]:
        """특정 기능에 속한 모든 요구사항을 조회합니다."""
        pass

    @abstractmethod
    async def get_by_status(self, status: str) -> List[Requirement]:
        """특정 상태의 모든 요구사항을 조회합니다."""
        pass