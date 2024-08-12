from sqlalchemy.ext.asyncio import AsyncSession

from .texts import TextDAO
from .users import UserDAO


class HolderDAO:
    users: UserDAO
    texts: TextDAO

    __slots__ = ("users", "texts")

    def __init__(self, *, session: AsyncSession) -> None:
        self.users = UserDAO(session=session)
        self.texts = TextDAO(session=session)
