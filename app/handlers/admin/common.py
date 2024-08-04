from pathlib import Path

from aiogram import Router, F
from aiogram.types import Message, FSInputFile

from aiofiles import open as async_open

from app.database import Database

common_router = Router()


@common_router.message(F.text == "Количество пользователей")
async def get_count_users(message: Message, db: Database):
    count_users = await db.users.get_count_users()
    await message.answer(f"Количество пользователей: {count_users}")


@common_router.message(F.text == "Вывод пользователей")
async def get_users(message: Message, db: Database):
    users = await db.users.get_all_users()
    abs_path = Path(__file__).parent
    result = ""

    for user in users:
        result += f"{user.user_id} | @{user.username}\n"

    async with async_open(f"{abs_path}/users.txt", "w") as file:
        await file.write(result)

    file = FSInputFile(path=f"{abs_path}/users.txt")

    await message.answer_document(
        document=file,
        caption="Вот файл со всеми пользователями!"
    )
