from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from app.callback_factory import EditTextFactory


def get_admin_menu() -> ReplyKeyboardMarkup:
    name_functions_for_admin = [
        "Рассылка",
        "Редактировать текст",
        "Количество пользователей",
        "Вывод пользователей",
    ]

    keyboard = ReplyKeyboardBuilder()
    for title_button in name_functions_for_admin:
        keyboard.button(text=title_button)

    return keyboard.as_markup(resize_keyboard=True)


def get_break_menu() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text="Отмена")
    return keyboard.as_markup(resize_keyboard=True)


def get_keyboard_with_url(name_button: str, url: str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=name_button, url=url)
    return keyboard.as_markup()


def get_texts_menu() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    texts = {
        "Основной": "main_text",
        "Инструкция": "manual_text",
        "Нету подписки": "not_sub_text",
    }
    for text, callback in texts.items():
        keyboard.button(text=text, callback_data=EditTextFactory(menu=callback))

    keyboard.adjust(2)
    return keyboard.as_markup()
