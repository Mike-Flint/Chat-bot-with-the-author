from aiogram.types import InlineKeyboardMarkup , InlineKeyboardButton

kb_raffle = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Участвовать", callback_data="raffle"),
            ],
        ]
    )

kb_buy = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="", callback_data="back_buy"),
                InlineKeyboardButton(text="Створити заявку", callback_data="Create_application")
            ],
        ]
    )

kb_write = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Назад", callback_data="back_write"),
                InlineKeyboardButton(text="Аутентификация", callback_data="authentication")
            ],
        ]
    )