from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

shaurma2124154856 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Shaurma qalampir mol go'sht"),
            KeyboardButton("Shaurma tovuq go'sht")
        ],
        [
            KeyboardButton("Shaurma qalampir tovuq go'sht"),
            KeyboardButton("Shaurma mol go'sht")
        ]
    ], resize_keyboard=True
)