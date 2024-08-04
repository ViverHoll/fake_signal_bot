from aiogram import Router

from . import select_options


def setup_all_dialogs() -> Router:
    router = Router()

    select_options.setup(router)

    return router
