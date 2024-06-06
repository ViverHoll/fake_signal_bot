from aiogram import Router

from .signal import router as signal_router
from .start import router as start_router
from .user import router as user_router

from .admin.commands import router as admin_router
from .admin.func_admin import router as func_admin_router

handlers_router = Router()
handlers_router.include_routers(
    admin_router,
    func_admin_router,
    start_router,
    signal_router,
    user_router
)
