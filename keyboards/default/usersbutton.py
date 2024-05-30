from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('📲Telefon raqamini yuborish', request_contact=True),
        ]
    ], resize_keyboard=True
)

obsh = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('🍴 Menyu')

        ],
        [
            KeyboardButton('📋 Mening buyurtmalarim')
        ],
        [
            KeyboardButton('📥 Savat'),
            KeyboardButton('📞 Aloqa')
        ],
        [
            KeyboardButton('📨 Xabar yuborish'),
            KeyboardButton('⚙️ Sozlamalar')
        ],
        [
            KeyboardButton('ℹ️ Biz haqimizda')
        ]
    ],resize_keyboard=True
)