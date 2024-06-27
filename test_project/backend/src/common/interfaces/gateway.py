import abc
from types import TracebackType
from typing import TypeVar, AsyncContextManager, Optional, Type

GatewayType = TypeVar("GatewayType", bound="BaseGateway")


class BaseGateway(abc.ABC):
    def __init__(self, context_manager: AsyncContextManager) -> None:
        self.__context_manager = context_manager

    async def __aenter__(self) -> GatewayType:
        await self.__context_manager.__aenter__()
        return self

    async def __aexit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_value: Optional[BaseException],
            traceback: Optional[TracebackType],
    ) -> None:
        await self.__context_manager.__aexit__(exc_type, exc_value, traceback)
