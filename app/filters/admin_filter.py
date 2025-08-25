from aiogram.types import Message
from aiogram.filters import Filter

from config import config


class AdminProtect(Filter):
    def __init__(self):
        self.admins = config.bot.admins

    async def __call__(self, message: Message):
        return message.from_user.id in self.admins