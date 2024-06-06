from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery

from database import Database
from keyboards.user import main_menu, get_button_with_data, after_registration_menu

router = Router()
_back_callbacks = ["back_registration", "back_main_menu"]


@router.callback_query(F.data == "manual")
async def get_manual(callback: CallbackQuery, db: Database):
    keyboard = get_button_with_data("Вернуться назад", "back_main_menu")
    menu = await db.texts.get_texts()

    await callback.message.edit_text(menu.manual,
                                     reply_markup=keyboard)


@router.callback_query(F.data == "manual_signal")
async def get_manual(callback: CallbackQuery, db: Database):
    keyboard = get_button_with_data("Вернуться назад", "back_after_sub_menu")

    menu = await db.texts.get_texts()
    await callback.message.edit_text(menu.manual,
                                     reply_markup=keyboard)


@router.callback_query(F.data.in_(_back_callbacks))
async def back_to_main_meny(
        callback: CallbackQuery,
        bot: Bot,
        db: Database
):
    name_bot = await bot.get_my_name()
    menu = await db.texts.get_texts()

    await callback.message.edit_text(
        menu.main_menu.format(name_bot.name),
        reply_markup=main_menu
    )


@router.callback_query(F.data == "back_after_sub_menu")
async def get_after_sub_menu(
        callback: CallbackQuery,
        bot: Bot,
        db: Database
):
    bot_name = await bot.get_my_name()
    menu = await db.texts.get_texts()

    await callback.message.edit_text(
        menu.main_menu.format(bot_name),
        reply_markup=after_registration_menu
    )
