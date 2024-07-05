from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI

from backend.src.api.v1.endpoints import setup_routers
from backend.src.core.settings import Settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    yield
    await app.state.engine.dispose()


def init_app(setting: Settings) -> FastAPI:
    app = FastAPI(
        title="TEST_PROJECT",
        lifespan=lifespan,
    )
    setup_routers(app)
    return app
