from fastapi import FastAPI

from backend.src.api.setup import init_app
from backend.src.core.run_uvicorn import run_uvicorn
from backend.src.core.settings import load_setting, Settings


def main() -> None:
    settings: Settings = load_setting()
    app: FastAPI = init_app(settings)
    run_uvicorn(app, settings)


if __name__ == "__main__":
    main()
