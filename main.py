import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config_reader import config

from database import DatabaseMiddleware
from database.session import create_session_pool

from handlers import handlers_router
from state import states_router
from middlewares import (CheckSubMessageMiddleware,
                         CheckSubCallbackMiddleware,
                         CheckDataUserCallbackMiddleware,
                         CheckDataUserMessageMiddleware)


async def main():
    bot = Bot(
        token=config.BOT_TOKEN.get_secret_value(),
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
            link_preview_is_disabled=True
        )
    )
    dp = Dispatcher(
        storage=MemoryStorage()
    )

    dp["session_pool"] = create_session_pool(
        url=config.db_url
    )

    dp.message.middleware(DatabaseMiddleware())
    dp.callback_query.middleware(DatabaseMiddleware())

    dp.message.middleware(CheckDataUserMessageMiddleware())
    dp.callback_query.middleware(CheckDataUserCallbackMiddleware())

    dp.message.middleware(CheckSubMessageMiddleware())
    dp.callback_query.middleware(CheckSubCallbackMiddleware())

    dp.include_routers(
                       handlers_router,
                       states_router
                       )

    print("[+] --- bot online! --- [+]")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
