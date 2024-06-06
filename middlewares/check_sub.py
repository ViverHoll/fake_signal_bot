from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware, Bot
from aiogram.types import Message, CallbackQuery

from database import Database

from misc.utils import username_channel

from keyboards.user import not_sub_menu


class CheckSubMessageMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        bot: Bot = data["bot"]
        db: Database = data["db"]

        self.menu = await db.texts.get_texts()
        self.status_user = await bot.get_chat_member(
            chat_id=username_channel,
            user_id=event.from_user.id
        )

        if self.status_user.status == 'left':
            await event.answer(
                text=self.menu.not_sub,
                reply_markup=not_sub_menu
            )
        else:
            return await handler(event, data)


class CheckSubCallbackMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        bot: Bot = data["bot"]
        db: Database = data["db"]

        self.menu = await db.texts.get_texts()
        self.status_user = await bot.get_chat_member(
            chat_id=username_channel,
            user_id=event.from_user.id
        )

        if self.status_user.status == 'left':
            await event.message.answer(
                text=self.menu.not_sub,
                reply_markup=not_sub_menu
            )
        else:
            return await handler(event, data)
