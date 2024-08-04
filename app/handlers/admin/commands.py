from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.keyboards.admin import get_admin_menu

commands_router = Router()


@commands_router.message(Command("admin"))
async def command_start_admin(message: Message):
    await message.answer(
        "<b><i>Добро пожаловать в админ-панель!</i></b>",
        reply_markup=get_admin_menu()
    )
