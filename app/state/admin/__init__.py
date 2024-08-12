from aiogram import Router

from .edit_text import router as edit_text_router
from .mailing import router as mailing_router

admin_state_router = Router()
admin_state_router.include_routers(
    mailing_router,
    edit_text_router
)
