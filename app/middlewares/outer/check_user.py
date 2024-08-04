from typing import Awaitable, Any, Callable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User

from app.database import Database


class CheckDataUserMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: dict[str, Any]
    ) -> Any:
        db: Database = data["db"]

        user: User = data["event_from_user"]
        if not user:
            return await handler(event, data)

        parameters = {
            "user_id": user.id,
            "username": user.username
        }

        if not user:
            await db.users.add_user(**parameters)
            return await handler(event, data)

        if user.username != event.from_user.username:
            await db.users.update_username(**parameters)

        return await handler(event, data)

