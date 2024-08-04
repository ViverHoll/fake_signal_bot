from aiogram.fsm.state import State, StatesGroup


class OptionsMainMenu(StatesGroup):
    main = State()
    registration = State()
    manual = State()
    signal = State()
