from app.infrastructure.database.models.base_model import PersistenceModel
from sqlalchemy.orm import DeclarativeMeta, DeclarativeBase
from abc import ABCMeta

class ABCDeclarativeMeta(ABCMeta, DeclarativeMeta):
    pass

class SQLAlchemyModel(DeclarativeBase, PersistenceModel, metaclass=ABCDeclarativeMeta):
    __abstract__ = True