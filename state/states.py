from aiogram.fsm.state import State, StatesGroup


class Registration(StatesGroup):
    win_id = State()
    signal = State()


class Mailing(StatesGroup):
    message = State()
    image = State()
    keyboard = State()


class EditText(StatesGroup):
    menu_text = State()
    new_text = State()


class EditUrl(StatesGroup):
    new_url = State()
