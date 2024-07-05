import uuid
from typing import Any, overload

from backend.src.database.converter import from_model_to_dto
from backend.src.database.exceptions import DatabaseError
from backend.src.database.repositories.user import UserRepository
from backend.src.common.dto.user import UserInDB, CreateUser


class UserService:
    __slots__ = ("_repository",)

    def __init__(self, repository: UserRepository) -> None:
        self._repository = repository

    async def create(self, data: CreateUser) -> UserInDB:
        result = await self._repository.create_user(**data.model_dump())
        if not result:
            raise DatabaseError("User is defined")
        return from_model_to_dto(result, UserInDB)

    @overload
    async def get_one(self, *, user_id: uuid.UUID) -> UserInDB: ...
    @overload
    async def get_one(self, *, tg_id: int) -> UserInDB: ...

    async def get_one(self, **kw: Any) -> UserInDB:
        result = await self._repository.get_one(**kw)
        if not result:
            raise DatabaseError("User is not defined")
        return from_model_to_dto(result, UserInDB)

