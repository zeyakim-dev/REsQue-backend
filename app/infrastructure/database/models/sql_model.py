from abc import ABCMeta
from uuid import UUID

from sqlalchemy.orm import DeclarativeBase, DeclarativeMeta, Mapped, mapped_column

from app.infrastructure.database.models.base_model import PersistenceModel


class ABCDeclarativeMeta(ABCMeta, DeclarativeMeta):
    pass


class SQLAlchemyModel(DeclarativeBase, PersistenceModel, metaclass=ABCDeclarativeMeta):
    __abstract__ = True

    id: Mapped[UUID] = mapped_column()
