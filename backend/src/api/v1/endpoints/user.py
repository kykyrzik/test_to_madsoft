from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from backend.src.api.response import OkResponse
from backend.src.common.dto.user import UserInDB, CreateUser
from backend.src.api.v1.handlers.user.create import command_create_user

user_router = APIRouter(prefix="/user", tags=["User"])


@user_router.post("/create",
                  response_model=UserInDB,
                  status_code=status.HTTP_201_CREATED)
async def create_user(body: CreateUser,
                      ) -> OkResponse[UserInDB]:
    result: UserInDB = await command_create_user(body)
    return OkResponse(result, status_code=status.HTTP_201_CREATED)
