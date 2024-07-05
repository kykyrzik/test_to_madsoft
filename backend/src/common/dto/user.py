from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class CreateUser(BaseModel):
    tg_id: int
    username: str


class UserInDB(CreateUser):
    uuid: UUID
    started_at: datetime
    updated_at: datetime
