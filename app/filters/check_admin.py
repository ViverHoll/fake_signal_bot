from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsAdmin(BaseFilter):
    def __init__(self):
        self.admins = ["айди администраторов"]

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admins
