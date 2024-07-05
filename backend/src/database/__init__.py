from typing import Type, Callable

from backend.src.database.core.connectioin import SessionFactoryType
from backend.src.database.core.manager import TransactionManager
from backend.src.database.gateway import DBGateway


def create_database_factory(manager: Type[TransactionManager],
                            session_factory: SessionFactoryType
                            ) -> Callable[[], DBGateway]:
    def _create() -> DBGateway:
        return DBGateway(manager(session_factory()))

    return _create
