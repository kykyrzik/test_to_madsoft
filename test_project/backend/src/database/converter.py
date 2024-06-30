from typing import TypeVar, Type

from pydantic import BaseModel

from test_project.backend.src.database.models.base.base import ModelType


DTOModel = TypeVar("DTOModel", bound=BaseModel)


def from_model_to_dto(value: ModelType, dto: Type[DTOModel]) -> DTOModel:
    return dto(**value.__dict__)
