from collections.abc import Awaitable, Callable
from typing import Any

from aiogram import BaseMiddleware, Dispatcher
from aiogram.types import TelegramObject

from .session import SessionPool
from .dao import HolderDAO


class DatabaseMiddleware(BaseMiddleware):
    def setup(self, *, dispatcher: Dispatcher) -> None:
        dispatcher.update.outer_middleware.register(self)

    async def __call__(
            self,
            handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: dict[str, Any]
    ) -> Any:
        session_pool: SessionPool = data["session_pool"]

        async with session_pool() as session:
            data["db"] = HolderDAO(session=session)
            return await handler(event, data)


