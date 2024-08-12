from typing import Any, Generic, TypeVar

from sqlalchemy import insert, select, text, update
from sqlalchemy.ext.asyncio import AsyncSession

from .models import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)


async def update_by_where(self, *whereclause: Any, **values: Any):
    stmt = update(self.model).values(**values).returning(self.model)
    if whereclause:
        stmt = stmt.where(*whereclause)
    return await self.session.execute(stmt)


class Repository(Generic[ModelType]):
    session: AsyncSession
    model: type[ModelType]

    __slots__ = ("session", "model")

    def __init__(self, session: AsyncSession, model: type[ModelType]) -> None:
        self.session = session
        self.model = model

    def add(self, *, entity: ModelType) -> ModelType:
        self.session.add(instance=entity)
        return entity

    async def insert_data(self, **values):
        query = insert(self.model).values(**values)
        return await self.session.execute(query)

    async def update_by_where(self, *whereclause: Any, **values: Any):
        query = update(self.model).values(**values)
        if whereclause:
            query = query.where(*whereclause)
        return await self.session.execute(query)

    async def get_by_where(self, *whereclause, column: str = "*"):
        query = select(text(column)).select_from(self.model)
        if whereclause:
            query = query.where(*whereclause)
        return await self.session.execute(query)

    async def commit(self) -> None:
        return await self.session.commit()
