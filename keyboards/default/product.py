from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menyu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Setlar (8)')
        ],
        [
            KeyboardButton('Lavash (9)'),
            KeyboardButton('Shaurma (4)')
        ],
        [
            KeyboardButton('Burger (4)'),
            KeyboardButton('Hot dog (8)')
        ],
        [
            KeyboardButton('Ichimliklar (11)')
        ],
        [
            KeyboardButton('Shirinlik va disertlar (4)')
        ],
        [
            KeyboardButton('Garnirlar (10)')
        ],
        [
            KeyboardButton('🔙Orqaga qaytish')
        ]
    ]
)