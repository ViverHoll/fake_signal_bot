from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import TextModel
from app.database.repository import Repository
from app.types_data import Text


class TextDAO:
    repository: Repository[TextModel]

    __slots__ = ("repository",)

    def __init__(self, session: AsyncSession) -> None:
        self.repository = Repository(session=session, model=TextModel)

    async def get_texts(self) -> Text:
        texts = (await self.repository.get_by_where()).all()
        return Text(*texts[0])

    async def update_text(self, **texts: Any) -> None:
        await self.repository.update_by_where(**texts)
        await self.repository.commit()
