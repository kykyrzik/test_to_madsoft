from typing import TypeVar

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.declarative import declared_attr


ModelType = TypeVar("ModelType", bound="Base")


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
