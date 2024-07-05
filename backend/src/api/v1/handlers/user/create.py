from typing import Any, Annotated

from fastapi import Depends

from backend.src.common.dto.user import CreateUser, UserInDB
from backend.src.services.gateway import ServiceGateway


async def command_create_user[CreateUser, UserInDB](query: CreateUser,
                                                    gateway: Annotated[ServiceGateway, Depends()],
                                                    ) -> UserInDB:
    async with gateway:
        return await gateway.user().create(query)
