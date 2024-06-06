from aiogram import Router

from .registration import router as registration_router

from .admin import admin_state_router

states_router = Router()
states_router.include_routers(
    admin_state_router,
    registration_router
)
