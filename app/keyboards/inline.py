from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import config

admin_panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Рассылка", callback_data="sender")],
        [InlineKeyboardButton(text="Администраторы", callback_data="admins")],
    ]
)

admin_cancel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back")]
    ]
)

check_sub = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Подписаться", url=config.bot.channel_link)],
        [InlineKeyboardButton(text="Проверить подписку", callback_data="check_sub")]
    ]
)
