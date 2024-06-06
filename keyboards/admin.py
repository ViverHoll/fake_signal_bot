from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           InlineKeyboardButton)
from aiogram.utils.keyboard import (ReplyKeyboardBuilder,
                                    InlineKeyboardBuilder)


from callback_factory import EditTextFactory

name_functions_for_admin = [
    "Рассылка",
    "Редактировать текст",
    "Количество пользователей",
    "Вывод пользователей"
]


def get_admin_menu() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    for title_button in name_functions_for_admin:
        keyboard.button(text=title_button)

    keyboard.adjust(1)
    return keyboard.as_markup(resize_keyboard=True)


def get_break_menu() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text="Отмена")
    # keyboard.adjust(1)
    return keyboard.as_markup(resize_keyboard=True)


def get_keyboard_with_url(name_button: str, url: str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=name_button, url=url)
    return keyboard.as_markup()


def get_texts_menu() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    texts = {
        "Основной": "main",
        "Инструкция": "manual",
        "Нету подписки": "not_sub"
    }
    for text, callback in texts.items():
        keyboard.button(
            text=text,
            callback_data=EditTextFactory(
                menu=callback
            )
        )

    keyboard.adjust(2)
    return keyboard.as_markup()
