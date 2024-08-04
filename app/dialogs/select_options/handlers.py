from aiogram.types import CallbackQuery, Message

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import ManagedTextInput

from app.dialogs.states import OptionsMainMenu
from app.keyboards.user import get_after_registration_menu


async def reg_button(
        callback: CallbackQuery,
        button: Button,
        dialog_manager: DialogManager
):
    await dialog_manager.switch_to(OptionsMainMenu.registration)


async def manual_button(
        callback: CallbackQuery,
        button: Button,
        dialog_manager: DialogManager
):
    await dialog_manager.switch_to(OptionsMainMenu.manual)


async def back_button(
        callback: CallbackQuery,
        button: Button,
        dialog_manager: DialogManager
):
    await dialog_manager.switch_to(OptionsMainMenu.main)


def check_win_id(win_id: str) -> str:
    if win_id.isdigit() and len(win_id) == 8:
        return win_id
    raise ValueError


async def input_correct_win_id(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str
):
    await dialog_manager.done()

    await message.answer(
        "Вы успешно прошли регистрацию!",
        reply_markup=get_after_registration_menu()
    )




async def error_win_id_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        error: ValueError
):
    await message.answer("Вы ввели некорректный айди")
