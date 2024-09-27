from abc import ABCMeta

from sqlalchemy.orm import DeclarativeBase, DeclarativeMeta

from app.infrastructure.database.models.base_model import PersistenceModel


class ABCDeclarativeMeta(ABCMeta, DeclarativeMeta):
    pass


class SQLAlchemyModel(DeclarativeBase, PersistenceModel, metaclass=ABCDeclarativeMeta):
    __abstract__ = True
