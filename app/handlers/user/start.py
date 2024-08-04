from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from aiogram_dialog import DialogManager, StartMode

from app.dialogs.states import OptionsMainMenu

start_router = Router()


@start_router.message(CommandStart())
async def command_start(
        *args,
        dialog_manager: DialogManager
):
    await dialog_manager.start(
        OptionsMainMenu.main,
        mode=StartMode.RESET_STACK
    )


@start_router.callback_query(F.data == 'check_sub')
async def start_bot(
        *args,
        dialog_manager: DialogManager
):
    await dialog_manager.start(
        OptionsMainMenu.main,
        mode=StartMode.RESET_STACK
    )


@start_router.message(Command("status"))
async def cmd_status(message: Message):
    await message.answer("Вы используете последнюю версию бота #2")
