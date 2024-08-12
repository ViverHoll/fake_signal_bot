from aiogram import F, Router
from aiogram.types import CallbackQuery

from app.database import Database
from app.keyboards.user import get_after_registration_menu, get_button_with_data

user_router = Router()


@user_router.callback_query(F.data == "manual_signal")
async def get_manual(callback: CallbackQuery, db: Database):
    keyboard = get_button_with_data("Вернуться назад", "back_after_sub_menu")

    menu = await db.texts.get_texts()
    await callback.message.edit_text(menu.manual, reply_markup=keyboard)


@user_router.callback_query(F.data == "back_after_sub_menu")
async def get_after_sub_menu(callback: CallbackQuery, db: Database):
    menu = await db.texts.get_texts()

    await callback.message.edit_text(
        menu.main_menu, reply_markup=get_after_registration_menu()
    )
