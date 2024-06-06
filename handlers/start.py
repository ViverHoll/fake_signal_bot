from aiogram import Router, Bot, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery


from keyboards.user import main_menu
from database import Database

router = Router()


@router.message(CommandStart())
async def command_start(
        message: Message,
        bot: Bot,
        db: Database
):

    name_bot = await bot.get_my_name()
    menu = await db.texts.get_texts()

    await message.answer(
        menu.main_menu.format(name_bot.name),
        reply_markup=main_menu,
        parse_mode='html'
    )


@router.callback_query(F.data == 'check_sub')
async def start_bot(callback: CallbackQuery, bot: Bot, db: Database):
    name_bot = await bot.get_my_name()
    menu = await db.texts.get_texts()

    await callback.message.answer(
        menu.not_sub.format(name_bot.name),
        reply_markup=main_menu
    )


@router.message(Command("status"))
async def cmd_status(message: Message):
    await message.answer("Вы используете последнюю версию бота #2")
