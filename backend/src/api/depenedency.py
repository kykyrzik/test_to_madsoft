from typing import Callable, TypeVar

from fastapi import FastAPI


from backend.src.core.settings import Settings
from backend.src.database import create_database_factory
from backend.src.database.core.connectioin import create_sa_engine, create_sa_session_factory
from backend.src.database.core.manager import TransactionManager
from backend.src.services import create_service_gateway_factory, ServiceGateway

DependencyType = TypeVar("DependencyType")


def singleton(value: DependencyType) -> Callable[[], DependencyType]:
    def singleton_factory() -> DependencyType:
        return value

    return singleton_factory


def setup_dependencies(app: FastAPI, settings: Settings) -> None:
    engine = create_sa_engine(settings.db.url)
    app.state.engine = engine
    session_factory = create_sa_session_factory(engine)
    database_factory = create_database_factory(TransactionManager, session_factory)
    service_factory = create_service_gateway_factory(database_factory)

    app.dependency_overrides[ServiceGateway] = service_factory
