from typing import Unpack, overload, Optional, Sequence, Type
import uuid

from backend.src.database.models import User
from backend.src.database.exceptions import InvalidParamsError
from .base import BaseRepository
from .types.user import CreateUserType


class UserRepository(BaseRepository[User]):
    @property
    def model(self) -> Type[User]:
        return self.model

    async def create_user(self, **data: Unpack[CreateUserType]) -> Optional[User]:
        return await self._crud.insert(**data)

    @overload
    async def get_one(self, *, user_id: uuid.UUID) -> Optional[User]: ...

    @overload
    async def get_one(self, *, tg_id: int) -> Optional[User]: ...

    async def get_one(
            self,
            *,
            user_id: Optional[uuid.UUID] = None,
            tg_id: Optional[int] = None
    ) -> Optional[User]:
        if not any([user_id, tg_id]):
            raise InvalidParamsError("at least one identifier must be provided")

        clause = self.model.id == user_id if user_id else self.model.tg_id == tg_id

        return await self._crud.select(clause)

    async def get_many(self,
                       offset: Optional[int] = None,
                       limit: Optional[int] = None
                       ) -> Sequence[User]:
        return await self._crud.select_many(offset=offset, limit=limit)
