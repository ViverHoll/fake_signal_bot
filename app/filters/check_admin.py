from aiogram.types import Message
from aiogram.filters import BaseFilter


class IsAdmin(BaseFilter):
    def __init__(self):
        # self.admins = config.ADMINS
        self.admins = ['айди администраторов']

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admins
