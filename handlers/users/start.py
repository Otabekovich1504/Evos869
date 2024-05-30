from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.usersbutton import contact
from keyboards.default.usersbutton import obsh
from loader import dp






@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    await message.answer('<b>EVOS | Доставка</b> botiga xush kelibsiz!',reply_markup=contact)
    await message.answer('''
Avval telefon raqamingizni yuboring,
yoki +998XX XXXXXXX ko'rinishida yozing.

https://evos.uz/uz/about/    
    ''')

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def contact1(message: types.Message):
    await message.reply('Telefon raqamingiz qabul qilindi✅')
    await message.answer('<b>🛒 Asosiy Menyu</b>')
    await message.answer('Marhamat buyurtma berishingiz mumkin!', reply_markup=obsh)

