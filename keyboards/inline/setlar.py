from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='-', callback_data='-'),
            InlineKeyboardButton(text='1', callback_data='1'),
            InlineKeyboardButton(text='+', callback_data='+')
        ],
        [
            InlineKeyboardButton(text='📥Savatga kochirish', callback_data='savat    ')
        ]
    ]
)