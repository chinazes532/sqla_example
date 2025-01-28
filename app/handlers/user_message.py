import datetime

from aiogram import Router, Bot, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, Callback

import app.keyboards.reply as rkb
import app.keyboards.inline as ikb
import app.keyboards.builder as bkb

from app.filters.admin_filter import AdminProtect

from app.database.requests.user.add import set_user

user = Router()


@user.message(CommandStart())
async def start_command(message: Message):
    admin = AdminProtect()
    current_date = datetime.datetime.now().strftime("%d.%m.%Y")
    if not await admin(message):  
        await message.answer(f"Привет, {message.from_user.full_name}!\n")
        await set_user(message.from_user.id, message.from_user.full_name, current_date)
    else:
        await message.answer(f"Привет, {message.from_user.full_name}!\n")
        await set_user(message.from_user.id, message.from_user.full_name, current_date)
        await message.answer(f"Вы успешно авторизовались как администратор!",
                             reply_markup=rkb.admin_menu)

