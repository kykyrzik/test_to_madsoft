from test_project.backend.src.common.interfaces.gateway import BaseGateway
from test_project.backend.src.database.core.manager import TransactionManager
from test_project.backend.src.database.repositories.user import UserRepository


class DBGateway(BaseGateway):
    __slots__ = ("manager",)

    def __init__(self, manager: TransactionManager) -> None:
        self.manager = manager
        super().__init__(manager)

    def user(self):
        return UserRepository(self.manager.session)
