from backend.src.common.interfaces.gateway import BaseGateway
from backend.src.database.gateway import DBGateway
from backend.src.services.user import UserService


class ServiceGateway(BaseGateway):
    def __init__(self, gateway: DBGateway):
        self.database_gateway = gateway
        super().__init__(gateway)

    def user(self) -> UserService:
        return UserService(self.database_gateway.user())
