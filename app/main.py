import asyncio

from app.factory import create_app_config, create_bot, create_dispatcher


async def main():
    config = create_app_config()

    bot = create_bot(config)
    dp = create_dispatcher(config)

    print("[+] --- bot online! --- [+]")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
