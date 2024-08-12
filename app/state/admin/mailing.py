import asyncio
from typing import Literal, Union

from aiogram import Bot, F, Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, Message

from app.database import HolderDAO
from app.keyboards.admin import get_admin_menu, get_break_menu, get_keyboard_with_url
from app.state.states import Mailing

router = Router()


@router.message(F.text == "Рассылка")
async def start_mailing_fsm(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Введите сообщение для рассылки:", reply_markup=get_break_menu()
    )
    await state.set_state(Mailing.message)


@router.message(F.text == "Отмена")
async def break_fsm(message: Message, state: FSMContext):
    await message.answer("Вы успешно завершили ввод", reply_markup=get_admin_menu())
    await state.clear()


@router.message(Mailing.message, F.text)
async def get_message_for_mailing(message: Message, state: FSMContext):
    await state.update_data(message_mailing=message.html_text)
    await message.answer(
        "Если вы хотите добавить кнопку для рассылки, то пришлите сообщение в формате:"
        "название кнопки|ссылка\n"
        'Если вы не хотите добавлять кнопку, то напишите слово "нет"'
    )
    await state.set_state(Mailing.keyboard)


@router.message(Mailing.keyboard, F.text)
async def get_keyboard_user(message: Message, state: FSMContext):
    if "|" in message.text:
        name_button, url = message.text.split("|")
        await state.update_data(
            keyboard=get_keyboard_with_url(name_button, url.lstrip())
        )
    else:
        await state.update_data(keyboard=None)
    await message.answer(
        "Отлично! Теперь пришлите фото или видео\n"
        'Если не хотите присылать, просто пришлите "."'
    )
    await state.set_state(Mailing.image)


@router.message(Mailing.image, F.photo)
async def get_photo_user(message: Message, state: FSMContext, db: HolderDAO, bot: Bot):
    file_id = message.photo[0].file_id
    data_user = await state.get_data()
    all_users = await db.users.get_all_id_users()
    await mailing(
        data_user["message_mailing"],
        all_users,
        message.from_user.id,
        bot,
        data_user["keyboard"],
        file_id,
        "photo",
        "photo",
    )
    await message.answer("Рассылка завершена!", reply_markup=get_admin_menu())
    await state.clear()


@router.message(Mailing.image, F.video)
async def get_video_user(message: Message, state: FSMContext, db: HolderDAO, bot: Bot):
    file_id = message.video.file_id
    data_user = await state.get_data()
    all_users = await db.users.get_all_id_users()
    await mailing(
        data_user["message_mailing"],
        all_users,
        message.from_user.id,
        bot,
        data_user["keyboard"],
        file_id,
        "video",
        "video",
    )
    await message.answer("Рассылка завершена!", reply_markup=get_admin_menu())
    await state.clear()


@router.message(Mailing.image, F.text)
async def get_message_user(
        message: Message, state: FSMContext, db: HolderDAO, bot: Bot
):
    data_user = await state.get_data()
    all_users = await db.users.get_all_id_users()
    await mailing(
        data_user["message_mailing"],
        all_users,
        message.from_user.id,
        bot,
        data_user["keyboard"],
        type_message="text",
    )
    await message.answer("Рассылка завершена!", reply_markup=get_admin_menu())
    await state.clear()


async def mailing(
        text: str,
        all_users: list,
        admin_id: Union[str, int],
        bot: Bot,
        keyboard: InlineKeyboardMarkup = None,
        file_id: str = None,
        type_image: str = None,
        type_message: Literal["text", "photo", "video"] = None,
) -> None:
    dict_values = {"text": text, "reply_markup": keyboard, "parse_mode": "html"}

    type_send_message = {
        "photo": bot.send_photo,
        "video": bot.send_video,
        "text": bot.send_message,
    }
    if file_id:
        del dict_values["text"]

        dict_values[type_image] = file_id
        dict_values["caption"] = text

    for user in all_users:
        try:
            await type_send_message[type_message](chat_id=user, **dict_values)
            await asyncio.sleep(0.3)
        except TelegramBadRequest as Error:
            await bot.send_message(
                chat_id=admin_id,
                text="Произошла ошибка при отправке сообщения:\n"
                     f"<i>{Error}</i>\n"
                     f"<b><i>{type(Error)}</b></i>",
            )
        except Exception as Error:
            await bot.send_message(
                chat_id="АДМИН АЙДИ",
                text=f"Произошла ошибка: {type(Error)}\n\n{Error}",
                parse_mode=None,
            )
        finally:
            await asyncio.sleep(0.3)
