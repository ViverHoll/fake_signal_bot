from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent


class Setting:
    BOT_TOKEN: SecretStr

    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/database/db.db"

    model_config = SettingsConfigDict(
        env_file="config.env",
        env_file_encoding="utf-8"
    )


config = Setting()
