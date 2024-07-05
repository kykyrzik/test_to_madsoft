import abc
from typing import Generic, TypeVar, Mapping, Any, Optional, Sequence, Protocol, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession

EntryType = TypeVar("EntryType")

RepositoryType = TypeVar("RepositoryType", bound="Repository")


class Repository(Protocol):
    def __init__(self, session: AsyncSession) -> None: ...


class AbstractCRUDRepository(abc.ABC, Generic[EntryType]):
    def __init__(self, model: EntryType) -> None:
        self.model = model

    @abc.abstractmethod
    async def insert(self, **values: Mapping[str, Any]) -> EntryType:
        raise NotImplementedError

    @abc.abstractmethod
    async def select(self, *clauses: Any) -> Optional[EntryType]:
        raise NotImplementedError

    @abc.abstractmethod
    async def select_many(
            self, *clauses: Any, offset: Optional[int] = None, limit: Optional[int] = None
    ) -> Sequence[EntryType]:
        raise NotImplementedError

    @abc.abstractmethod
    async def update(
        self, *clauses: Any, **values: Mapping[str, Any]
    ) -> Sequence[EntryType]:
        raise NotImplementedError

    @abc.abstractmethod
    async def delete(self, *clauses: Any) -> Sequence[EntryType]:
        raise NotImplementedError
