from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup


def get_after_registration_menu() -> InlineKeyboardMarkup:
    """Функция для получения клавиатуры после регистрации"""
    buttons = {"Инструкция": "manual_signal", "Получить сигналы": "get_signal"}

    keyboard = InlineKeyboardBuilder()

    for name, callback in buttons.items():
        keyboard.button(text=name, callback_data=callback)

    return keyboard.as_markup()


def get_not_sub_menu(url: str) -> InlineKeyboardMarkup:
    """Функция для получения меню, если нет подписки"""
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Подписаться на канал", url=url)

    keyboard.button(text="Проверить подписку", callback_data="check_sub")
    return keyboard.as_markup()


def get_button_with_data(name_button: str, callback: str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text=name_button, callback_data=callback)

    keyboard.adjust(1)
    return keyboard.as_markup()
