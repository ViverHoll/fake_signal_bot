from typing import TypeAlias

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

SessionPool: TypeAlias = async_sessionmaker[AsyncSession]


def create_session_pool(*, url: URL | str, echo: bool = False) -> SessionPool:
    engine = create_async_engine(url=url, echo=echo)

    return async_sessionmaker(
        bind=engine, autoflush=False, expire_on_commit=False, autocommit=False
    )
