from aiogram import Router

from .start import start_router
from .signal import signal_router
from .user import user_router

user_handler_router = Router()
user_handler_router.include_routers(
    start_router,
    signal_router,
    user_router
)
