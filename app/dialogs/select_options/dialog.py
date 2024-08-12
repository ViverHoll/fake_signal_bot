from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button, Column, Url
from aiogram_dialog.widgets.text import Const, Format

from app.dialogs.states import OptionsMainMenu

from .getters import get_texts
from .handlers import (
    back_button,
    check_win_id,
    error_win_id_handler,
    input_correct_win_id,
    manual_button,
    reg_button,
)

main_menu_dialog = Dialog(
    Window(
        Format("{main_text}"),
        Column(
            Button(
                text=Const("Регистрация"), id="registration_button", on_click=reg_button
            ),
            Button(
                text=Const("Инструкция"), id="manual_button", on_click=manual_button
            ),
            Button(
                text=Const("Выдать сигнал"), id="signal_button", on_click=reg_button
            ),
        ),
        state=OptionsMainMenu.main,
        getter=get_texts,
    ),
    Window(
        Format("{main_text}"),
        TextInput(
            id="input_win_id",
            type_factory=check_win_id,
            on_success=input_correct_win_id,
            on_error=error_win_id_handler,
        ),
        Column(
            Url(text=Const("Регистрация"), url=Format("{win_ref_url}")),
            Button(text=Const("Назад"), id="cancel_button", on_click=back_button),
        ),
        state=OptionsMainMenu.registration,
        getter=get_texts,
    ),
    Window(
        Format("{manual_text}"),
        Button(text=Const("Назад"), id="cancel_button", on_click=back_button),
        state=OptionsMainMenu.manual,
        getter=get_texts,
    ),
)
