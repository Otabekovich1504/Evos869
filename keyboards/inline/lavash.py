from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


lavashbtn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='-', callback_data='-'),
            InlineKeyboardButton(text='1', callback_data='1'),
            InlineKeyboardButton(text='+', callback_data='+')
        ],
        [
            InlineKeyboardButton(text='📥Savatga kochirish', callback_data='savat')
        ]
    ]
)

lavashbtn2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Mini 25 000 so`m', callback_data='mini25'),
            InlineKeyboardButton(text="Big 29 000 so`m", callback_data='big29')
        ]
    ]
)

lavashbtn3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mini 23 000 so'm", callback_data="mini23"),
            InlineKeyboardButton(text="Big 27 000 so'm", callback_data="big27")
        ]
    ]
)

lavashbtn4 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mini 20 000 so'm", callback_data='mini20'),
            InlineKeyboardButton(text="Big 24 000 so'm", callback_data='big24')
        ]
    ]
)
lavashbtn5 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mini 22 000 so'm", callback_data='mini22'),
            InlineKeyboardButton(text="Big 26 000 so'm", callback_data='big26')
        ]
    ]
)