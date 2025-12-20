from aiogram.fsm.state import State, StatesGroup


class AddAdmin(StatesGroup):
    tg_id = State()


class SendAll(StatesGroup):
    text = State()