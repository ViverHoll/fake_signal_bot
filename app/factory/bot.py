from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.app_config import AppConfig


def create_bot(config: AppConfig) -> Bot:
    return Bot(
        token=config.common.bot_token.get_secret_value(),
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
            link_preview_is_disabled=True
        )
    )
