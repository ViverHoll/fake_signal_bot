from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from database import Database
from keyboards.admin import get_texts_menu
from state.states import EditText
from callback_factory import EditTextFactory

router = Router()


@router.message(F.text == "Редактировать текст")
async def start_fsm_edit_text(message: Message, state: FSMContext):
    await message.answer("Выберите текст который нужно изменить:",
                         reply_markup=get_texts_menu()
                         )
    await state.set_state(EditText.menu_text)


# Сделать тут фабрику коллбэков
@router.callback_query(
    EditText.menu_text,
    EditTextFactory.filter()
)
async def get_menu_text(
        callback: CallbackQuery,
        state: FSMContext,
        callback_data: EditTextFactory
):
    await callback.message.edit_text(
        "Отлично! Теперь введите новый текст"
    )

    await state.update_data(menu=callback_data.menu)
    await state.set_state(EditText.new_text)


@router.message(EditText.new_text, F.text)
async def get_new_text(
        message: Message,
        state: FSMContext,
        db: Database
):
    menu_text = (await state.get_data()).get("menu")
    if menu_text == "main":
        await db.texts.update_text(main_text=message.html_text)
    if menu_text == "manual":
        await db.texts.update_text(manual_text=message.html_text)
    if menu_text == "not_sub":
        await db.texts.update_text(not_sub_text=message.html_text)

    await message.answer("Текст успешно изменен")
    await state.clear()
