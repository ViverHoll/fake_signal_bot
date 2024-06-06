from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from misc.utils import url_channel, win_ref_url

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Регистрация",
                callback_data="registration"
            ),
            InlineKeyboardButton(
                text="Инструкция",
                callback_data="manual"
            )
        ],
        [
            InlineKeyboardButton(
                text="Выдать сигнал",
                callback_data="signal_registration"
            )
        ]
    ]
)


def get_registration_keyboard(win_url: str) -> InlineKeyboardMarkup:
    """Функция для генерации клавиатуры со ссылкой на 1win"""
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text="Регистрация",
        url=win_url
    )
    keyboard.button(
        text="Назад",
        callback_data="back_registration"
    )
    keyboard.adjust(1)
    return keyboard.as_markup()


def get_button_url_and_back_button() -> InlineKeyboardMarkup:
    """Функция для генерации клавиатуры со ссылкой и кнопкой в главное меню"""
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text="Регистрация",
        url=win_ref_url
    )
    keyboard.button(
        text="Назад",
        callback_data="back_main_menu"
    )
    keyboard.adjust(1)
    return keyboard.as_markup()


after_registration_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Инструкция",
                callback_data="manual_signal"
            )
        ],
        [
            InlineKeyboardButton(
                text="Получить сигналы",
                callback_data="get_signal"
            )
        ]
    ]
)

not_sub_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Подписаться на канал",
                url=url_channel
            )
        ],
        [
            InlineKeyboardButton(
                text="Проверить подписку",
                callback_data="check_sub"
            )
        ]
    ]
)

# back_to_main_menu = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(
#                 text="Вернуться назад",
#                 callback_data="back_main_menu"
#             )
#         ]
#     ]
# )
#
# signal_menu = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(
#                 text="Получить сигнал",
#                 callback_data="get_signal"
#             )
#         ]
#     ]
# )


def get_button_with_data(
        name_button: str,
        callback: str
) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text=name_button,
        callback_data=callback
    )
    keyboard.adjust(1)
    return keyboard.as_markup()
