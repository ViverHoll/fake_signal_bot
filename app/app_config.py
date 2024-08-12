from pathlib import Path

from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings as BaseSettings_
from pydantic_settings import SettingsConfigDict
from sqlalchemy import URL


class BaseSettings(BaseSettings_):
    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent / "config.env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


class CommonConfig(BaseSettings, env_prefix="COMMON_"):
    bot_token: SecretStr


class PostgresConfig(BaseSettings, env_prefix="POSTGRES_"):
    host: str
    db_name: str
    password: SecretStr
    user: str

    def build_url(self):
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.user,
            password=self.password.get_secret_value(),
            host=self.host,
            database=self.db_name,
        )


class WinConfig(BaseSettings, env_prefix="WIN_"):
    ref_url: str


class ChannelConfig(BaseSettings, env_prefix="CHANNEL_"):
    url: str
    username: str


class AppConfig(BaseModel):
    common: CommonConfig
    postgres: PostgresConfig
    win: WinConfig
    channel: ChannelConfig
