from aiogram.types import Message
from aiogram.filters import BaseFilter

from config_reader import config


class IsAdmin(BaseFilter):
    def __init__(self):
        self.admins = config.ADMINS

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admins
