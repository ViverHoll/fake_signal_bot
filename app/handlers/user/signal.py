import asyncio
import os
from random import randint, random, triangular

from aiogram import F, Router
from aiogram.types import CallbackQuery, FSInputFile

from app.func import add_text_on_photo
from app.keyboards.user import get_button_with_data

signal_router = Router()


def get_random_float_value(
        start: float = 92.31,
        end: float = 98.74,
) -> float:
    random_float_value = triangular(start, end)
    return round(random_float_value, 2)


def get_bet() -> float:
    chance = random()
    start = 1.13
    end = 3.23

    if 0.8 > chance > 0.1:
        end = 5.23
    elif 0.8 > chance > 0.07:
        end = 10.23
    elif 0.8 > chance > 0.02:
        end = 20.23
    elif 0.8 > chance > 0.01:
        end = 100.23

    return get_random_float_value(start, end)


@signal_router.callback_query(F.data == "get_signal")
async def get_signal(callback: CallbackQuery):
    # random_value = get_random_float_value(1.13, 3.23)
    await callback.answer()

    info_message = await callback.message.answer("Получаю информацию")
    await asyncio.sleep(0.5)

    random_value = get_bet()
    win_percent = get_random_float_value()

    await info_message.edit_text("Анализирую ставки")
    await asyncio.sleep(0.5)

    abs_path_result_photo = os.path.abspath("image/lucky_jet_new.jpg")
    number_game = randint(10_932, 97_837)

    await info_message.edit_text("Отправляю запрос")
    await asyncio.sleep(0.5)

    add_text_on_photo(
        text=f"{random_value}",
        photo_path=os.path.abspath("image/lucky_jet.jpg"),
        new_path_photo=abs_path_result_photo,
    )

    photo = FSInputFile(path=abs_path_result_photo)

    await info_message.edit_text("Получаю сигнал")
    await asyncio.sleep(0.5)
    keyboard = get_button_with_data("Получить сигнал", "get_signal")

    await info_message.delete()
    await callback.message.answer_photo(
        photo=photo,
        caption=f"🚀 Игра №{number_game}\n\nШанс - {win_percent}%",
        reply_markup=keyboard,
    )
