from typing import Awaitable, Any, Callable

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from database import Database


class CheckDataUserMessageMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: dict[str, Any]
    ) -> Any:
        db: Database = data["db"]

        user = await db.users.get_info_user(event.from_user.id)

        if not user or user.username != event.from_user.username:
            await db.users.update_username(
                user_id=event.from_user.id,
                username=event.from_user.username
            )
        return await handler(event, data)


class CheckDataUserCallbackMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[CallbackQuery, dict[str, Any]], Awaitable[Any]],
            event: CallbackQuery,
            data: dict[str, Any]
    ) -> Any:
        db: Database = data["db"]

        user = await db.users.get_info_user(event.from_user.id)

        if not user or user.username != event.from_user.username:
            await db.users.update_username(
                user_id=event.from_user.id,
                username=event.from_user.username
            )
        return await handler(event, data)
