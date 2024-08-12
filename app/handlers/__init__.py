from aiogram import Router

from .admin import admin_router
from .user import user_handler_router

handlers_router = Router()
handlers_router.include_routers(admin_router, user_handler_router)
