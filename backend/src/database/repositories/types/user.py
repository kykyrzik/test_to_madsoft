from typing import TypedDict
from typing_extensions import Required


class CreateUserType(TypedDict):
    tg_id: Required[int]
    username: Required[str]
