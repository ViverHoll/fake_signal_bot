from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware, Bot
from aiogram.types import TelegramObject, User, CallbackQuery

from app.database import Database

from app.app_config import AppConfig

from app.keyboards.user import get_not_sub_menu


class CheckSubMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        bot: Bot = data["bot"]
        db: Database = data["db"]
        config: AppConfig = data["config"]

        user: User = data["event_from_user"]
        if not user:
            return await handler(event, data)

        self.menu = await db.texts.get_texts()
        self.status_user = await bot.get_chat_member(
            chat_id=config.channel.username,
            user_id=user.id
        )

        if self.status_user.status == 'left':
            parameters = {
                "text": self.menu.not_sub,
                "reply_markup": get_not_sub_menu(
                    url=config.channel.url
                )
            }

            if isinstance(event, CallbackQuery):
                await event.message.answer(**parameters)
            else:
                await event.answer(**parameters)
        else:
            return await handler(event, data)
