from app.app_config import (
    AppConfig,
    CommonConfig,
    PostgresConfig,
    WinConfig,
    ChannelConfig
)


def create_app_config() -> AppConfig:
    return AppConfig(
        common=CommonConfig(),
        postgres=PostgresConfig(),
        win=WinConfig(),
        channel=ChannelConfig()
    )
