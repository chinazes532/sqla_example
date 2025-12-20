import datetime

from aiogram import Router, Bot, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

import app.keyboards.reply as rkb
import app.keyboards.inline as ikb
import app.keyboards.builder as bkb

from app.database.requests.admin.select import get_admins
from app.database.requests.user.add import set_user

user = Router()


@user.callback_query(F.data == "check_sub")
async def check_sub(callback: CallbackQuery):
    current_date = datetime.datetime.now().strftime("%d.%m.%Y")
    
    await callback.message.edit_text("Спасибо за подписку, вы можете пользоваться ботом!")

    await set_user(callback.from_user.id, callback.from_user.full_name, current_date)


@user.message(CommandStart())
async def start_command(message: Message):
    current_date = datetime.datetime.now().strftime("%d.%m.%Y")
    await set_user(message.from_user.id, message.from_user.full_name, current_date)

    await message.answer("Добро пожаловать!")

    admins = await get_admins()

    for admin in admins:
        if admin.tg_id == message.from_user.id:
            await message.answer(f"Вы успешно авторизовались как администратор!",
                                 reply_markup=rkb.admin_menu)
            return

