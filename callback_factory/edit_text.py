from aiogram.filters.callback_data import CallbackData


class EditTextFactory(CallbackData, prefix="edit_text"):
    menu: str



