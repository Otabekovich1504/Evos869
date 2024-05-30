from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

lavash = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Mol goʼshtidan qalampir lavash'),
            KeyboardButton('Tovuq goʼshtli qalampir lavash')
        ],
        [
            KeyboardButton('Mol goʼshtidan pishloqli lavash Standard'),
            KeyboardButton("Lavash cheese tovuq go'sht Standart")
        ],
        [
            KeyboardButton("FITTER"),
            KeyboardButton("Lavash tovuq go'sht")
        ],
        [
            KeyboardButton("Lavash mol go'sht")
        ],
        [
            KeyboardButton("🔙Orqaga qaytish")
        ]
    ],resize_keyboard=True
)