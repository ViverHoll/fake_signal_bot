from aiogram import Router

from .mailing import router as mailing_router
from .edit_text import router as edit_text_router

admin_state_router = Router()
admin_state_router.include_routers(
    mailing_router,
    edit_text_router
)


