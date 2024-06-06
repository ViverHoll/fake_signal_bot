from typing import Any, Optional

from sqlalchemy.ext.asyncio import AsyncSession

from database.models import TextModel
from database.repository import Repository

from types_data import Text


class TextDAO:
    repository: Repository[TextModel]

    __slots__ = ("repository",)

    def __init__(self, session: AsyncSession) -> None:
        self.repository = Repository(
            session=session,
            model=TextModel
        )

    async def get_texts(self) -> Text:
        texts = (await self.repository.get_by_where()).all()
        return Text(*texts[0])

    async def update_text(self, **texts: Any) -> None:
        await self.repository.update_by_where(**texts)
        await self.repository.commit()
