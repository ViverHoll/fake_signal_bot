from aiogram.filters.callback_data import CallbackData


class EditTextFactory(CallbackData, prefix="edit_"):
    menu: str
