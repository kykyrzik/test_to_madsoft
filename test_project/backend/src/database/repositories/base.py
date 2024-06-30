import abc
from typing import Generic, Type

from sqlalchemy.ext.asyncio import AsyncSession

from test_project.backend.src.database.models.base.base import ModelType
from test_project.backend.src.database.repositories.crud import BaseCRUD


class BaseRepository(Generic[ModelType]):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
        self._crud = BaseCRUD(self.model, session)

    @property
    @abc.abstractmethod
    def model(self) -> Type[ModelType]:
        raise NotImplementedError
