from aiogram_dialog import DialogManager
from typing_extensions import Any

from app.app_config import AppConfig
from app.database import Database


async def get_texts(
        dialog_manager: DialogManager,
        **kwargs: Any
):
    db: Database = dialog_manager.middleware_data["db"]
    config: AppConfig = dialog_manager.middleware_data["config"]

    texts = await db.texts.get_texts()

    return {
        "main_text": texts.main_menu,
        "manual_text": texts.manual,
        "win_ref_url": config.win.ref_url
    }

