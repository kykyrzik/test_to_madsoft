from typing import Any, Optional, Sequence, Mapping, Type

import sqlalchemy as sql
from sqlalchemy.ext.asyncio import AsyncSession

from backend.src.common.interfaces.repository import AbstractCRUDRepository
from backend.src.database.models.base.base import ModelType


class BaseCRUD(AbstractCRUDRepository[ModelType]):
    def __init__(self, model: ModelType, session: AsyncSession) -> None:
        super().__init__(model)
        self._session = session

    async def insert(self, **values:  Any) -> Optional[ModelType]:
        stmt = sql.insert(self.model).values(**values).returning(self.model)
        return (await self._session.execute(stmt)).scalars().first()

    async def select(self, *clauses: Any) -> Optional[ModelType]:
        stmt = sql.select(self.model).where(*clauses)
        return (await self._session.execute(stmt)).scalars().first()

    async def select_many(self,
                          *clauses: Any,
                          offset: Optional[int] = None,
                          limit: Optional[int] = None
                          ) -> Sequence[ModelType]:
        stmt = sql.select(self.model).where(*clauses).offset(offset).limit(limit)
        return (await self._session.execute(stmt)).scalars().all()

    async def update(self, *clauses: Any, **values: Mapping[str, Any]) -> Sequence[ModelType]:
        stmt = sql.update(self.model).where(*clauses).values(**values)
        return (await self._session.execute(stmt)).scalars().all()

    async def delete(self, *clauses: Any) -> Sequence[ModelType]:
        stmt = sql.update(self.model).where(*clauses)
        return (await self._session.execute(stmt)).scalars().all()
