from aiogram import Router

from .admin import admin_state_router

states_router = Router()
states_router.include_routers(
    admin_state_router,
)
