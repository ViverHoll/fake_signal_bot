from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from filters import IsAdmin
from keyboards.admin import get_admin_menu

router = Router()
router.message.filter(IsAdmin())


@router.message(Command("admin"))
async def command_start_admin(message: Message):
    await message.answer(
        "Добро пожаловать в админ-панель!",
        reply_markup=get_admin_menu()
    )
