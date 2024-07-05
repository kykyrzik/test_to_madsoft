from fastapi import APIRouter, FastAPI

from backend.src.api.v1.endpoints.user import user_router


def setup_routers(app: FastAPI) -> None:
    app.include_router(user_router)
