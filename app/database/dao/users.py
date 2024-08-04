from app.types_data import User

from app.database.models import UserModel
from app.database.repository import Repository

from sqlalchemy.ext.asyncio import AsyncSession


class UserDAO:
    repository: Repository[UserModel]

    __slots__ = ("repository",)

    def __init__(self, *, session: AsyncSession) -> None:
        self.repository = Repository(
            session=session,
            model=UserModel
        )

    async def add_user(self, **values):
        await self.repository.insert_data(**values)
        await self.repository.commit()

    async def get_count_users(self) -> int:
        users = await self.repository.get_by_where()
        return len(users.all())

    async def get_info_user(self, user_id: int) -> list | User:
        result = await self.repository.get_by_where(
            UserModel.user_id == user_id
        )

        info = result.all()

        if info:
            return User(*info[0])
        return []

    async def update_username(self, user_id: int, username: str) -> None:
        await self.repository.update_by_where(
            UserModel.user_id == user_id,
            username=username
        )
        await self.repository.commit()

    async def get_all_id_users(self) -> list[int]:
        users = await self.repository.get_by_where()
        return [
            user[0]
            for user in users.all()
        ]

    async def get_all_users(self) -> list[User]:
        users = (await self.repository.get_by_where()).all()
        return [
            User(*user)
            for user in users
        ]
