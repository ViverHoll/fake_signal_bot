from aiogram.types import Message
from aiogram.filters import BaseFilter


class IsAdmin(BaseFilter):
    def __init__(self, admin: int = 789080569):
        if not isinstance(admin, int):
            raise TypeError("Необходимо передать целое число!")
        self.admins = [1258093139, 789080569]

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admins
