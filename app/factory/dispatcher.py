from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from aiogram_dialog import setup_dialogs

from app_config import AppConfig

from app.database import DatabaseMiddleware
from app.database.session import create_session_pool

from app.middlewares.outer import (CheckDataUserMiddleware,
                                   CheckSubMiddleware)

from app.handlers import handlers_router
from app.state import states_router

from app.dialogs import setup_all_dialogs


def _setup_inner_middleware(dispatcher: Dispatcher):
    dispatcher.message.middleware(CheckDataUserMiddleware())
    dispatcher.message.middleware(CheckSubMiddleware())

    dispatcher.callback_query.middleware(CheckDataUserMiddleware())
    dispatcher.callback_query.middleware(CheckSubMiddleware())


def _setup_outer_middleware(dispatcher: Dispatcher):
    dispatcher.update.outer_middleware(DatabaseMiddleware())


def create_dispatcher(config: AppConfig) -> Dispatcher:
    dispatcher = Dispatcher(
        config=config,
        storage=MemoryStorage(),
        session_pool=create_session_pool(
            url=config.postgres.build_url()
        )
    )

    _setup_outer_middleware(dispatcher)
    _setup_inner_middleware(dispatcher)

    dispatcher.include_routers(
        handlers_router,
        states_router,
        setup_all_dialogs()
    )
    setup_dialogs(dispatcher)

    return dispatcher
