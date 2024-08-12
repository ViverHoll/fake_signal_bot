from app.app_config import (
    AppConfig,
    ChannelConfig,
    CommonConfig,
    PostgresConfig,
    WinConfig,
)


def create_app_config() -> AppConfig:
    return AppConfig(
        common=CommonConfig(),
        postgres=PostgresConfig(),
        win=WinConfig(),
        channel=ChannelConfig(),
    )
