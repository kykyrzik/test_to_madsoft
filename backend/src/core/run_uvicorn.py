from typing import Any

import uvicorn

from backend.src.core.settings import Settings


def run_uvicorn(app: Any, config: Settings, **kw: Any) -> None:
    uv_config = uvicorn.Config(
        app,
        host=config.api_setting.host,
        port=config.api_setting.port,
        **kw,
    )
    server = uvicorn.Server(uv_config)
    server.run()
