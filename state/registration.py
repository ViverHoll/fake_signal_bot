from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from .states import Registration

from misc.utils import win_ref_url
from misc.texts import main_text

from keyboards.user import (get_registration_keyboard,
                            get_button_url_and_back_button,
                            after_registration_menu)

router = Router()

_allowed_callback = ["signal_registration", "registration"]


@router.callback_query(F.data.in_(_allowed_callback))
async def start_registration(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        main_text,
        reply_markup=get_registration_keyboard(
            win_url=win_ref_url
        )
    )
    await state.set_state(Registration.win_id)


@router.message(Registration.win_id, F.text)
async def get_win_id(message: Message,
                     state: FSMContext,
                     bot: Bot):
    if message.text.isdigit() and len(message.text) == 8:
        bot_name = await bot.get_my_name()

        text = (f'Вы успешно прошли регистрацию!\n\n'
                f'{main_text.format(bot_name)}')

        await message.answer(
            text,
            reply_markup=after_registration_menu
        )
        await state.clear()
    else:
        await message.answer(
            "Введён неверный айди, пройдите регистрацию еще раз!",
            reply_markup=get_button_url_and_back_button()
        )
