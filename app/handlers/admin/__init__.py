from aiogram import Router

from app.filters import IsAdmin

from .commands import commands_router
from .common import common_router

admin_router = Router()
admin_router.message.filter(IsAdmin())

admin_router.include_routers(common_router, commands_router)
